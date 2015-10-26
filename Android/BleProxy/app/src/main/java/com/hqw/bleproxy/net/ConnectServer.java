package com.hqw.bleproxy.net;

import android.os.Handler;

import com.hqw.bleproxy.LogUtil;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;
import java.net.SocketTimeoutException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Administrator on 2015/10/22.
 */
public class ConnectServer implements Runnable {

    private static final String TAG = ConnectServer.class.getSimpleName();
    public static final int MSG_CLIENT_CONNECTED = 10;
    public static final int MSG_CLIENT_DISCONNECTED = 11;
    private static int TIMEOUT = 100;

    private static ConnectServer mInstance ;
    private ServerSocket mServerSocket;
    private Thread mThread;
    private List<ProxyServer> mProxyServerList;
    private Handler mHandler;

    private ConnectServer() {
        mProxyServerList = new ArrayList<>();
    }

    public synchronized static ConnectServer getInstance() {
        if(mInstance == null) {
            mInstance = new ConnectServer();
        }
        return mInstance;
    }

    public boolean initServer() {
        try {
            mServerSocket = new ServerSocket(NetConfig.getServerPort(), 1);
            mServerSocket.setReuseAddress(true);
            mServerSocket.setSoTimeout(TIMEOUT);
            LogUtil.i(TAG, "init server ok -> " + mServerSocket.getLocalSocketAddress().toString() + ":" + NetConfig.getServerPort());
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }

        return true;
    }

    public void setHandler(Handler handler) {
        mHandler = handler;
    }

    public String getBindAddress() {
        try {
            return NetUtil.getLocalIpAddress() + ":" + NetConfig.getServerPort();
        } catch (SocketException e) {
            e.printStackTrace();
            return "";
        }
    }

    public boolean startServer() {
        if(mThread != null) {
            LogUtil.d(TAG, "already started");
            return true;
        }

        if(!initServer()) {
            return false;
        }
        mThread = new Thread(this);
        mThread.start();

        return true;
    }

    public boolean isRunning() {
        return mThread != null && mThread.isAlive();
    }

    public void stopServer() {
        try {
            mServerSocket.close();
            mServerSocket = null;
        } catch (IOException e) {
            e.printStackTrace();
        }

        for(ProxyServer proxyServer: mProxyServerList) {
            proxyServer.stop();
        }
    }

    @Override
    public void run() {
        if(mServerSocket == null) {
            return;
        }

//        Socket s;
        while(!mServerSocket.isClosed()) {
            try {
                final Socket s = mServerSocket.accept();
                ProxyServer proxyServer = new ProxyServer(s);
                final String remoteAddress =  s.getInetAddress().getHostAddress();
                if(mHandler != null) {
                    mHandler.obtainMessage(MSG_CLIENT_CONNECTED, remoteAddress).sendToTarget();
                }
                proxyServer.setOnProxyListener(new ProxyServer.OnProxyListener() {
                    @Override
                    public void clientDisconnected(ProxyServer proxyServer) {
                        mProxyServerList.remove(proxyServer);
                        proxyServer.stop();
                        mHandler.obtainMessage(MSG_CLIENT_DISCONNECTED,remoteAddress).sendToTarget();
                        LogUtil.d(TAG, "remove closed client");
                    }
                });
                new Thread(proxyServer).start();
                mProxyServerList.add(proxyServer);
                LogUtil.i(TAG, "New client connected: " + s.hashCode());

            } catch (SocketTimeoutException e) {
                continue;

            } catch (IOException e) {
                e.printStackTrace();
                break;
            }

        }

        mThread = null;
        LogUtil.i(TAG, "thread stopped");
    }
}
