package com.hqw.bleproxy.protocol;

/**
 * Created by Administrator on 2015/10/23.
 */
public class ProtocolPacker {

    private static ProtocolPacker mInstance;
    private BleProxy.BleProxyMsg.Builder mMsgBuilder;

    private ProtocolPacker() {
        mMsgBuilder = BleProxy.BleProxyMsg.newBuilder();
    }

    public synchronized static ProtocolPacker getInstance() {
        if(mInstance == null) {
            mInstance = new ProtocolPacker();
        }
        return mInstance;
    }

    public byte[] getConnectResultMsgBuff(boolean result, String errorString) {
        mMsgBuilder.clear();
        return mMsgBuilder.setCmd(BleProxy.ProxyMsgCmd.CONNECT_RESULT)
                .setConnectResult(BleProxy.ConnectResult.newBuilder().setResult(result)
                    .setErrorString(errorString)).build().toByteArray();
    }
}
