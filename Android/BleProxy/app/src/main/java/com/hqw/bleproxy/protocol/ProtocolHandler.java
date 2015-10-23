package com.hqw.bleproxy.protocol;

import com.google.protobuf.InvalidProtocolBufferException;
import com.hqw.bleproxy.BLEHelper;
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

            case BleProxy.ProxyMsgCmd.CONNECT_VALUE:
                onConnect(bleProxyMsg.getConnect());
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
        BLEHelper.getInstance().setOnBleListener(new BLEHelper.OnBleListener() {
            @Override
            public void onScanResult(String deviceName, String address, int rssi) {
                LogUtil.d(TAG, "deviceName: " + deviceName + ", address: " + address + ", rssi: " + rssi);
            }
        });
    }

    private void onStopScan() {
        LogUtil.d(TAG, "on stop scan");
        BLEHelper.getInstance().btStopScan();
    }

    private void onConnect(BleProxy.Connect connect) {
        LogUtil.d(TAG, "on connect device: " + connect.getAddress());
        if(!BLEHelper.getInstance().btConnect(null, connect.getAddress())) {
            // TODO: tell the client, connect error
        } else {
            // attention: even btConnect return true, we are not sure weather it's connected
            // we need broadcast
        }
    }
}
