package com.hqw.bleproxy;


import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothManager;
import android.content.Context;
import android.content.Intent;

import com.hqw.bleproxy.ble.BLEClient;
import com.hqw.bleproxy.ble.BLEConnManager;

public class BLEHelper {

	protected static final String TAG = BLEHelper.class.getSimpleName();
	private static BLEHelper mInstance;
	private BluetoothManager _bluetoothManager;
	private BluetoothAdapter _bluetoothAdapter;

	private OnBleListener mListener;

	private boolean _isConnecting = false;  // 是否正在连接BLE设备
//	private Map<String, Integer> _deviceInfo = new HashMap<String, Integer>();

	public interface OnBleListener {
		void onScanResult(String deviceName, String address, int rssi);
	}

	protected BluetoothAdapter.LeScanCallback _leScanCallback =  new BluetoothAdapter.LeScanCallback() {
		@Override
	    public void onLeScan(final BluetoothDevice device, int rssi, byte[] scanRecord) {
	        if(device == null) {
	            LogUtil.e(TAG, "device is null");
	            return;
	        }
	
//	        LogUtil.d(TAG, "device found: " + device.getName() + " # " + rssi );
	        String deviceName = device.getName();
	        String address = device.getAddress();
	        if(deviceName == null) {
	        	LogUtil.d(TAG, "ignore null name device");
	        	return;
	        }
			if(mListener != null) {
				mListener.onScanResult(deviceName, address, rssi);
			}
	    }
	};
        
	private BLEHelper() {
		_bluetoothManager = (BluetoothManager) BleProxyApp.getContext().getSystemService(Context.BLUETOOTH_SERVICE);
		assert _bluetoothManager != null;
		_bluetoothAdapter = _bluetoothManager.getAdapter();
	}

	public synchronized static BLEHelper getInstance() {
		if(mInstance == null) {
			mInstance = new BLEHelper();
		}
		return mInstance;
	}

	public void setOnBleListener(OnBleListener listener) {
		mListener = listener;
	}

	/**
	 * 检查手机是否支持蓝牙
	 * @return
	 */
	public boolean btIsBluetoothSupported() {
		return _bluetoothManager != null && _bluetoothAdapter  != null;
	}
	
	/**
	 * 检查蓝牙是否已打开
	 * @return
	 */
	public boolean btIsBluetoothOn() {
		return _bluetoothAdapter != null && _bluetoothAdapter.isEnabled();
	}
	/**
	 * 打开蓝牙
	 */
	public void btTurnOn(Activity activity, int requestCode) {
		Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
		activity.startActivityForResult(enableBtIntent, requestCode);
	}
	
	/**
	 * 启动BLE蓝牙设备扫描
	 */
	@SuppressWarnings("deprecation")
	public void btStartScan() {
		if(_bluetoothAdapter != null) {
			_bluetoothAdapter.startLeScan(_leScanCallback); 
		}
	}
	
	/**
	 * 停止BLE设备扫描
	 * 在不需要扫描的时候记得调用该函数关闭扫描，因为真的很费电
	 */
	@SuppressWarnings("deprecation")
	public void btStopScan() {
		if(_bluetoothAdapter != null) {
			_bluetoothAdapter.stopLeScan(_leScanCallback);
//			_deviceInfo.clear();
		}
	}
	
	/**
	 * 连接到BLE设备
	 * @param address
	 * 如果address为""，则连接到最近的设备
	 */
	public boolean btConnect(Context context, final String address) {
		if("".equals(address)) {
			return false;
		}
		if(context == null) {
			context = BleProxyApp.getContext();
		}
		return btConnectToDevice(context, address);
	}
	
	/**
	 * 断开BLE设备
	 * @param address
	 * 如果address为""，则断开所有已连接的设备
	 */
	public void btDisconnect(final String address) {
		BLEConnManager.getInstance().disconnect(address);
	}


	/**
	 *
	 * @param address
	 * @param buff
	 * @return
	 */
	public boolean btSend(String address, byte[] buff) {
		BLEClient client = BLEConnManager.getInstance().getLeClient(address);
		if(client == null) {
			LogUtil.d(TAG, "btSend error: client is null");
			return false;
		}
		LogUtil.d(TAG, "---------------Packet BUFF IS------------: " + StringUtil.bytesToHexString(buff));
		boolean ret = client.send(buff) == buff.length;
		if(ret) {
			LogUtil.d(TAG, "SEND OK");
		} else {
			LogUtil.e(TAG,  "SEND FAILED");
		}
		return ret;
	}

	/**
	 *
	 * @param address
	 * @param buff
	 * @param n
	 * @return
	 */
	public boolean btNSend(final String address, final byte[] buff, final int n) {
		if(n < 1) {
			return false;
		}
		new Thread(new Runnable() {
			@Override
			public void run() {
				btSend(address, buff);
				try {
					Thread.sleep(30);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		}).start();

		return true;
	}

	private boolean btConnectToDevice(Context context, final String address) {
		LogUtil.d(TAG, "------------------------------------------------");
		btStopScan();
		boolean result = BLEConnManager.getInstance().connect(context, address);
		if(!result) {
			// nothing
		} else {
			_isConnecting = true;
		}

		return result;
	}
	
	public boolean realBtConnect(String address) {
		_isConnecting = false;
		return BLEConnManager.getInstance().initLeClient(address);
	}
	
	public void dispatchBuff(String address, byte[] buff) {
    	LogUtil.d(TAG, "DATA From " + address + " --> " + StringUtil.bytesToHexString(buff));
    	BLEClient client = BLEConnManager.getInstance().getLeClient(address);
    	if(client == null) {
    		LogUtil.e(TAG, "BLEClient on " + address + " is null");
    		return;
    	}
    	client.handleReceivedBuff(buff);
    	LogUtil.d(TAG,  "BLEClient proc the data...");
	}

	public int getConnBLECount() {
		return BLEConnManager.getInstance().getConnBLECount();
	}
}
