#-*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = 1
import BleProxyMsg_pb2 as pb
import control_pb2 as ctrlpb
import socket
import logging
import struct
import threading
import select
import time
import binascii
import Queue

BLEPROXY_IP = "10.66.236.189"
BLEPROXY_PORT = 8927
#BLE_ADDRESS = "74:DA:EA:AE:9A:33" # FOR TEST
BLE_ADDRESS = "D0:5F:B8:2A:F6:E6"
#BLE_ADDRESS = "74:DA:EA:B1:09:7A"
INTERVAL = 0.2 # S
###################################################
MAX_WAIT_TIMES = 10
TURN_RIGHT_BUFF = "\x00\x0A\x08\x02\x22\x06\x08\x5A\x10\x02\x18\x2D\xF5"
TURN_LEFT_BUFF  = "\x00\x0A\x08\x02\x22\x06\x08\x5A\x10\x01\x18\x2D\xF4"
STOP_BUFF       = "\x00\x06\x08\x04\x32\x02\x08\x00\x4E"
ATTACK_BUFF     = "\x00\x06\x08\x06\x3A\x02\x08\x00\x58"
###################################################
bleConnected = False
seq = 1
sctpBuffQueue = Queue.Queue(maxsize=10)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logger = logging.getLogger("root")
countReq = 0
countAck = 0
startTime = 0

def initLogger():
    formatter = logging.Formatter("[%(levelname)-7s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s", "%d %b %Y %H:%M:%S")
    streamHandler = logging.StreamHandler(sys.stdout)
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)
    fileHandler = logging.FileHandler("debug.log")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)

def initSocket():
    sock.settimeout(0.5)
    
def dumpHex(data, addr=0, prefix=""):
        dump  = prefix
        slice = ""

        for byte in data:
            if addr % 16 == 0:
                dump += " "

                for char in slice:
                    if ord(char) >= 32 and ord(char) <= 126:
                        dump += char
                    else:
                        dump += "."

                dump += "\n  %s%04x: " % (prefix, addr)
                slice = ""

            dump  += "%02x " % ord(byte)
            slice += byte
            addr  += 1

        remainder = addr % 16

        if remainder != 0:
            dump += "   " * (16 - remainder) + " "

        for char in slice:
            if ord(char) >= 32 and ord(char) <= 126:
                dump += char
            else:
                dump += "."

        return dump + "\n"
        
def connectBleProxy(proxyAddr):
    try:
        sock.connect(proxyAddr)
        sock.setblocking(0)
        logger.info("connect %s:%d success" % proxyAddr)
        return True
    except Exception as e:
        logger.error("connect error")
        sys.exit(1)
    
def sendPbmsg(pbmsg):
        pbbuff = pbmsg.SerializeToString()
        lenbuff = struct.pack('H', len(pbbuff))
        n = 0
        try:
            n = sock.sendall(lenbuff + pbbuff)
        except:
            logger.error("bleproxy server closed")
            return
            
        if n:
            logger.error("send pb msg error, %d bytes sent, total: %d" % (n, len(pbbuff) + len(lenbuff)))
            
        return not n
        
def connectBleDevice(bleAddr):
    pbmsg = pb.BleProxyMsg()
    pbmsg.cmd = pb.CONNECT
    pbmsg.connect.address = bleAddr
    ret = sendPbmsg(pbmsg)
    if not ret:
        logger.error("connect ble device %s error: socket send error" % bleAddr)
    
    return ret

def handlePbBuff(pbBuff):
    global bleConnected, sock
    pbmsg = pb.BleProxyMsg()
    try:
        pbmsg.ParseFromString(pbBuff)
    except:
        logger.error("fail to parse pb buff")
        return
    
    if pbmsg.cmd == pb.CONNECT_RESULT:
        if pbmsg.connectResult.result:
            logger.info("connect ble device success")
            bleConnected = True
        else:
            logger.error("connect ble device failed: %s" % pbmsg.connectResult.errorStirng)
            sys.exit(1)
            
    elif pbmsg.cmd == pb.BLE_DISCONNECT:
        logger.error("BLE device disconnected")
        #TODO: reconnect
        sock.close()
        sock = None
        
    elif pbmsg.cmd == pb.PROXY_DATA:
        sctpBuff = pbmsg.proxyData.data
        sctpBuffQueue.put(pbmsg.proxyData.data)
        #print dumpHex(sctpBuff)
        # ctrlPbBuff = sctpBuff[5:-1]
        # ctrlMsg = ctrlpb.ControlMessage()
        # try:
            # ctrlMsg.ParseFromString(ctrlPbBuff)
            # if ctrlMsg.command == ctrlpb.ACK:
                # logger.debug("ACK: %d" % ctrlMsg.ack.seq)
        # except:
            # logger.error("CTRLMESSAGE PARSE ERROR: %s" % binascii.hexlify(sctpBuff))
            # #print dumpHex(ctrlPbBuff)
            
def SockReceiverTask():
    logger.debug("receiver task started")
    headBuff = ""
    bodyBuff = ""
    while sock:
        rfds, _, efds = select.select([sock], [], [sock], 0.1)
        if len(efds) > 0:
            logger.error("socket error")
            break
        
        if len(rfds) == 0:
            continue
        
        try:
            headBuff = sock.recv(2)    # len(lenbuff) may < 2, to be repaired
            assert len(headBuff) == 2  # tmp code
        except:
            logger.error("recv exp. recv head buff error")
            break
        if not headBuff:
            logger.error("bleproxy disconnected")
            break
            
        bodyLen = struct.unpack("H", headBuff)[0]
        #logger.debug("bodyLen is %d" % bodyLen)
        
        try:
            bodyBuff = sock.recv(bodyLen)    # 
            assert len(bodyBuff) == bodyLen  #
        except:
            logger.error("recv exp. recv body buff error")
            break
        
        #logger.debug(dumpHex(bodyBuff))
        handlePbBuff(bodyBuff)
    
    logger.error("receiver task stopped")
    if sock:
        sock.close()
        
    sys.exit(1)

WAIT_START = 0
WAIT_SEQ   = 1
WAIT_PORT  = 2
WAIT_SIZE  = 3
WAIT_DATA  = 4
WAIT_CRC   = 5
START_PARTEN = ("\xAA", "\xBB")
recvStatus = WAIT_START
def ctrlParseTask():
    global recvStatus, countAck
    buff = ""
    pos, seq, port, size = 0, 0, 0, 0
    pbDataBuff = []
    while recvTask.isAlive():
        try:
            buff = sctpBuffQueue.get(timeout=0.1)
        except:
            continue
            
        #logger.debug("GET SCTP Buff from queue: %s\n" % dumpHex(buff))
        for b in buff:
            if recvStatus == WAIT_START:
                if b == START_PARTEN[pos]:
                    pos += 1
                    if pos == len(START_PARTEN):
                        recvStatus = WAIT_SEQ
                        pos = 0
                else:
                    pos = 0
            
            elif recvStatus == WAIT_SEQ:
                seq = b
                recvStatus = WAIT_PORT
                
            elif recvStatus == WAIT_PORT:
                port = b
                recvStatus = WAIT_SIZE
            
            elif recvStatus == WAIT_SIZE:
                size = struct.unpack("B", b)[0]
                pbDataBuff = []
                recvStatus = WAIT_DATA
            
            elif recvStatus == WAIT_DATA:
                pbDataBuff.append(b)
                if len(pbDataBuff) == size:
                    recvStatus = WAIT_CRC
            
            elif recvStatus == WAIT_CRC:
                ctrlMsg = ctrlpb.ControlMessage()
                ctrlPbBuff = "".join(pbDataBuff)
                try:
                    ctrlMsg.ParseFromString(ctrlPbBuff)
                    if ctrlMsg.command == ctrlpb.ACK:
                        logger.info("ACK: %d" % ctrlMsg.ack.seq)
                        countAck += 1
                except:
                    logger.error("CTRLMESSAGE PARSE ERROR: \n%s" % dumpHex(buff))
                
                recvStatus = WAIT_START
                
recvTask = threading.Thread(target=SockReceiverTask)
parseTask = threading.Thread(target=ctrlParseTask)

def startRecvTask():
    recvTask.deamon = True
    recvTask.start()

def startParseTask():
    parseTask.deamon = True
    parseTask.start()
    
def sendProxyData(buff):
    global seq, countReq
    pbmsg = pb.BleProxyMsg()
    pbmsg.cmd = pb.PROXY_DATA
    pbmsg.proxyData.data = "\xAA\xBB" + struct.pack("B", seq) + buff
    ret = sendPbmsg(pbmsg)
    if ret:
        logger.info("REQ: %d" % seq)
        countReq += 1
    
    seq += 1
    if seq > 255:
        seq = 1
        
    return ret
        
def bleping():
    global bleConnected, startTime
    n = 0
    flag = True
    while 1:
        if not bleConnected:
            time.sleep(0.5)
            logger.debug("waiting connect result...")
            n += 1
            if n > MAX_WAIT_TIMES:
                logger.error("timeout, no response. please retry")
                break
            continue
        elif flag:
            startParseTask()
            startTime = time.time()
            flag = False
        
        if not sendProxyData(TURN_RIGHT_BUFF):
            logger.error("sock send error")
            break
        time.sleep(INTERVAL)
        if not sendProxyData(STOP_BUFF):
            logger.error("sock send error")
            break
        
        time.sleep(INTERVAL)
        
if __name__ == "__main__":
    initLogger()
    initSocket()
    if not connectBleProxy((BLEPROXY_IP, BLEPROXY_PORT)):
        logger.error("connect ble proxy failed")
        sys.exit(1)
    logger.debug("connect ble proxy %s:%d success" % (BLEPROXY_IP, BLEPROXY_PORT))
    startRecvTask()
    
    if not connectBleDevice(BLE_ADDRESS):
        logger.error("connect ble device %s failed" % BLE_ADDRESS)
        sys.exit(1)
    try:
        bleping()
    except KeyboardInterrupt:
        logger.debug("Stopping...")
        sock.close()
    
    logger.info("TIME COST: %d, COUNT OF REQ: %d, COUNT OF ACK: %d" % (time.time() - startTime, countReq, countAck))

    
    