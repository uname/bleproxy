package com.hqw.bleproxy.protocol;

import com.google.protobuf.InvalidProtocolBufferException;
import com.hqw.bleproxy.LogUtil;

/**
 * Created by Administrator on 2015/10/23.
 */
public class ProtocolHandler {

    private static final String TAG = ProtocolHandler.class.getSimpleName();

    public ProtocolHandler() {

    }

    private BleProxy.BleProxyMsg parseMsg(byte[] msgBuff) {
        try {
            BleProxy.BleProxyMsg bleProxyMsg = BleProxy.BleProxyMsg.parseFrom(msgBuff);
            return bleProxyMsg;
        } catch (InvalidProtocolBufferException e) {
            //e.printStackTrace();
            return null;
        }
    }

    public boolean handleMsg(byte[] msgBuff) {
        BleProxy.BleProxyMsg bleProxyMsg = parseMsg(msgBuff);
        if(bleProxyMsg == null) {
            LogUtil.e(TAG, "parseMsg error");
            return false;
        }

        LogUtil.d(TAG, "parseMsg success");
        switch (bleProxyMsg.getCmd().getNumber()) {
            case BleProxy.ProxyMsgCmd.CONTROL_VALUE:
                onControlMsg(bleProxyMsg.getControl());
                break;

            default:
                break;
        }
        return true;
    }

    private void onControlMsg(final BleProxy.Control controlMsg) {
        LogUtil.d(TAG, "onControl");
        switch (controlMsg.getCmd().getNumber()) {
            case BleProxy.ControlCmd.START_SCAN_VALUE:
                LogUtil.d(TAG, "on scan msg");
                break;
        }
    }
}
