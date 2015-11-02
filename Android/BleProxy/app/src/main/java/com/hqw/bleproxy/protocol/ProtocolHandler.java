package com.hqw.bleproxy.protocol;

import android.util.Log;

import com.google.protobuf.InvalidProtocolBufferException;
import com.hqw.bleproxy.BLEHelper;
import com.hqw.bleproxy.LogUtil;
import com.hqw.bleproxy.StringUtil;
import com.hqw.bleproxy.net.ProxyServer;

/**
 * Created by Administrator on 2015/10/23.
 */
public class ProtocolHandler {

    private static final String TAG = ProtocolHandler.class.getSimpleName();

    private ProxyServer mProxyServer;
    private BLEHelper.OnBleListener mListener = new BLEHelper.OnBleListener() {
        @Override
        public void onScanResult(String deviceName, String address, int rssi) {
            LogUtil.d(TAG, "deviceName: " + deviceName + ", address: " + address + ", rssi: " + rssi);
        }

        @Override
        public void onConnectResult(boolean result) {
            mProxyServer.send(ProtocolPacker.getInstance().getConnectResultMsgBuff(result, ""));
        }

        @Override
        public void onDisconnected() {
            mProxyServer.send(ProtocolPacker.getInstance().getBleDisconnectMsgBuff(""));
        }

        @Override
        public void onDataReceived(byte[] data) {
            LogUtil.d(TAG, "received: " + StringUtil.bytesToHexString(data));
            sendToClient(data);
        }
    };

    public ProtocolHandler(ProxyServer proxyServer) {
        BLEHelper.getInstance().setOnBleListener(mListener);
        mProxyServer = proxyServer;
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

            case BleProxy.ProxyMsgCmd.CONNECT_VALUE:
                onConnect(bleProxyMsg.getConnect());
                break;

            case BleProxy.ProxyMsgCmd.PROXY_DATA_VALUE:
                onSend(bleProxyMsg.getProxyData());
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
                onStartScan();
                break;

            case BleProxy.ControlCmd.STOP_SCAN_VALUE:
                onStopScan();
                break;
        }
    }

    private void onStartScan() {
        LogUtil.d(TAG, "on start scan");
        BLEHelper.getInstance().btStartScan();
    }

    private void onStopScan() {
        LogUtil.d(TAG, "on stop scan");
        BLEHelper.getInstance().btStopScan();
    }

    private void onConnect(BleProxy.Connect connectMsg) {
        LogUtil.d(TAG, "on connect device: " + connectMsg.getAddress());
        if(!BLEHelper.getInstance().btConnect(null, connectMsg.getAddress())) {
            mProxyServer.send(ProtocolPacker.getInstance().getConnectResultMsgBuff(false, ""));
        } else {
            // attention: even btConnect return true, we are not sure weather it's connected
            // we need broadcast
        }
    }

    private void onSend(BleProxy.ProxyData proxyData) {
        LogUtil.d(TAG, "on Send");
        byte[] data = proxyData.getData().toByteArray();
        BLEHelper.getInstance().btSend(null, data);
    }

    private void sendToClient(byte[] data) {
        mProxyServer.send(ProtocolPacker.getInstance().getProxyDataMsgBuff(data));
    }
}
