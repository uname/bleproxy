package com.hqw.bleproxy;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.hqw.bleproxy.net.ConnectServer;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = MainActivity.class.getSimpleName();
    public static int REQUEST_ENABLE_BT = 1;

    private Button   mServerSwitch;
    private TextView mServerStatus;
    private TextView mServerAddress;
    private TextView mServerLog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

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
    protected void onDestroy() {
        super.onDestroy();
        BLEHelper.getInstance().unRegisterBleBroadcastReceiver();
    }
}
