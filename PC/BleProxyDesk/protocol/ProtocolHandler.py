#-*- coding: utf-8 -*-
import BleProxyMsg_pb2 as bleProxyPb
import signals
from log import logger
from SigObject import sigObject

class ProtocolHandler:
    
    def __init__(self):
        self.msg = bleProxyPb.BleProxyMsg()
        self.cmdHandlerDict = {bleProxyPb.SCAN_RESULT: self.onScanResult,
                               bleProxyPb.CONNECT_RESULT: self.onConnectResult }
        
    def handleDataBuff(self, pbBuff):
        self.msg.Clear()
        try:
            self.msg.ParseFromString(pbBuff)
            handler = self.cmdHandlerDict.get(self.msg.cmd)
            if handler:
                handler()
            else:
                logger.error("unknown cmd %d" % self.msg.cmd)
            
        except Exception as e:
            print e
    
    def onScanResult(self):
        sigObject.emit(signals.SIG_BLE_DEVICE, self.msg.scanResult.name,
                       self.msg.scanResult.address,
                       self.msg.scanResult.rssi )
    
    def onConnectResult(self):
        sigObject.emit(signals.SIG_CONNECT_RESULT,  self.msg.connectResult.result,
            self.msg.connectResult.address, self.msg.connectResult.errorString)
        
protocolHandler = ProtocolHandler()