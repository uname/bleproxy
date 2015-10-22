package com.hqw.bleproxy.ble;

/**
 * Created by apache on 6/19/2015.
 */
public class BLEConnHolder {
    public BLEService bleService;
    public BLEClient bleClient;

    public BLEConnHolder(BLEService bleService) {
        this.bleService = bleService;
    }
}
