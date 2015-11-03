package com.hqw.bleproxy.protocol;

import com.google.protobuf.ByteString;

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

    public byte[] getScanResultMsgBuff(String deviceName, String address, int rssi) {
        mMsgBuilder.clear();
        return mMsgBuilder.setCmd(BleProxy.ProxyMsgCmd.SCAN_RESULT)
                .setScanResult(BleProxy.ScanResult.newBuilder().setName(deviceName).setAddress(address).setRssi(rssi)).build().toByteArray();
    }

    public byte[] getProxyDataMsgBuff(byte[] data) {
        mMsgBuilder.clear();
        return mMsgBuilder.setCmd(BleProxy.ProxyMsgCmd.PROXY_DATA)
                .setProxyData(BleProxy.ProxyData.newBuilder().setData(ByteString.copyFrom(data))).build().toByteArray();
    }

    public byte[] getBleDisconnectMsgBuff(String address) {
        mMsgBuilder.clear();
        return mMsgBuilder.setCmd(BleProxy.ProxyMsgCmd.BLE_DISCONNECT)
                .setBleDisconnect(BleProxy.BleDisconnect.newBuilder().setAddress(address)).build().toByteArray();
    }
}
