package com.hqw.bleproxy;

import android.content.Intent;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.hqw.bleproxy.net.ConnectServer;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = MainActivity.class.getSimpleName();
    public static int REQUEST_ENABLE_BT = 1;

    private Button   mServerSwitch;
    private TextView mServerStatus;
    private TextView mServerAddress;
    private TextView mServerLog;

    private boolean mExitFlag = false;

    private Handler mHandler = new Handler(new Handler.Callback() {
        @Override
        public boolean handleMessage(Message msg) {
            switch (msg.what) {
                case ConnectServer.MSG_CLIENT_CONNECTED:
                    addLog("connected: " + msg.obj);
                    break;

                case ConnectServer.MSG_CLIENT_DISCONNECTED:
                    addLog("disconnected: " + msg.obj);
                    BLEHelper.getInstance().btStopScan();
                    break;

                default:
                    break;
            }
            return false;
        }
    });

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ConnectServer.getInstance().setHandler(mHandler);

        initView();
    }

    private void initView() {
        mServerSwitch = (Button) findViewById(R.id.server_switch);
        mServerSwitch.setText(R.string.start_server);
        mServerStatus = (TextView) findViewById(R.id.server_status);
        mServerAddress = (TextView) findViewById(R.id.server_address);
        mServerAddress.setText(ConnectServer.getInstance().getBindAddress());
        mServerLog = (TextView) findViewById(R.id.server_log);
    }

    @Override
    protected void onResume() {
        super.onResume();
        if(!BLEHelper.getInstance().btIsBluetoothOn()) {
            BLEHelper.getInstance().btTurnOn(this, REQUEST_ENABLE_BT);
            return;
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    private void setUiOnStopped() {
        mServerSwitch.setText(R.string.start_server);
        mServerStatus.setText(R.string.status_stopped);
    }

    private void setUiOnStarted() {
        mServerSwitch.setText(R.string.stop_server);
        mServerStatus.setText(R.string.status_started);
        mServerLog.setText("");
    }

    private void addLog(String msg) {
        mServerLog.append(msg + "\n");
    }

    public void onServerSwitchClicked(View v) {
        if(ConnectServer.getInstance().isRunning()) {
            ConnectServer.getInstance().stopServer();
            setUiOnStopped();
        } else {
            if(ConnectServer.getInstance().startServer()) {
                setUiOnStarted();
            }
        }
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if(requestCode == REQUEST_ENABLE_BT && resultCode == RESULT_CANCELED) {
            finish();
            return;
        }
    }
    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if(keyCode != KeyEvent.KEYCODE_BACK) {
            return false;
        }

        if(mExitFlag) {
            finish();
            return false;
        }
        Toast.makeText(this, R.string.exit_tip, Toast.LENGTH_SHORT).show();
        mExitFlag = true;
        mHandler.postDelayed(new Runnable() {
            @Override
            public void run() {
                mExitFlag = false;
            }
        }, 3000);

        return false;
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        LogUtil.d(TAG, "onDestroy");
        BLEHelper.getInstance().unRegisterBleBroadcastReceiver();
        ConnectServer.getInstance().stopServer();
    }
}
