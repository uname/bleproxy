#-*- coding: utf-8 -*-

import BleProxyMsg_pb2 as bleProxyPb
import struct

class ProtocolPacker:
    
    def __init__(self):
        self.msg = bleProxyPb.BleProxyMsg()
    
    def __pack(self, pbBuff):
        size = len(pbBuff)
        return "%s%s" % (struct.pack("H", size), pbBuff)
        
    def getControlBuff(self, controlCmd):   
        self.msg.Clear()
        self.msg.cmd = bleProxyPb.CONTROL
        self.msg.control.cmd = controlCmd
        pbBuff = self.msg.SerializeToString()
        return self.__pack(pbBuff)
        
    def getStartScanBuff(self):
        return self.getControlBuff(controlCmd=bleProxyPb.START_SCAN)
        
    def getStopScanBuff(self):
        return self.getControlBuff(controlCmd=bleProxyPb.STOP_SCAN)
    
    def getConnectBuff(self, address):
        self.msg.Clear()
        self.msg.cmd = bleProxyPb.CONNECT
        self.msg.connect.address = address
        pbBuff = self.msg.SerializeToString()
        return self.__pack(pbBuff)
    
    def getDisconnectBuff(self, address=""):
        self.msg.Clear()
        self.msg.cmd = bleProxyPb.DISCONNECT
        self.msg.disconnect.address = address
        pbBuff = self.msg.SerializeToString()
        return self.__pack(pbBuff)
        
protocolPacker = ProtocolPacker()