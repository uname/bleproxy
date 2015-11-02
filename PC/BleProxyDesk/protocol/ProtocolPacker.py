#-*- coding: utf-8 -*-

import BleProxyMsg_pb2 as bleProxyPb

class ProtocolPacker:
    
    def __init__(self):
        self.msg = bleProxyPb.BleProxyMsg()
    
    def test(self):
        pass