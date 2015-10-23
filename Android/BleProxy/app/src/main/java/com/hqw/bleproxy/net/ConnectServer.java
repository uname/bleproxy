package com.hqw.bleproxy.net;

import com.hqw.bleproxy.LogUtil;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketTimeoutException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Administrator on 2015/10/22.
 */
public class ConnectServer implements Runnable {

    private static final String TAG = ConnectServer.class.getSimpleName();
    private static int SERVER_PORT = 8098;
    private static int TIMEOUT = 100;

    private static ConnectServer mInstance ;
    private ServerSocket mServerSocket;
    private Thread mThread;
    private List<ProxyServer> mProxyServerList;

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
            mServerSocket = new ServerSocket(SERVER_PORT, 1);
            mServerSocket.setReuseAddress(true);
            mServerSocket.setSoTimeout(TIMEOUT);
            LogUtil.i(TAG, "init server ok -> " + mServerSocket.getLocalSocketAddress().toString() + ":" + SERVER_PORT);
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }

        return true;
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

        Socket s;
        while(!mServerSocket.isClosed()) {
            try {
                s = mServerSocket.accept();
                ProxyServer proxyServer = new ProxyServer(s);
                proxyServer.setOnProxyListener(new ProxyServer.OnProxyListener() {
                    @Override
                    public void clientDisconnected(ProxyServer proxyServer) {
                        mProxyServerList.remove(proxyServer);
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
