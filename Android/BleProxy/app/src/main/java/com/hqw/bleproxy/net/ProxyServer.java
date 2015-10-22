package com.hqw.bleproxy.net;

import java.net.Socket;

/**
 * Created by Administrator on 2015/10/22.
 */
public class ProxyServer implements Runnable {

    private Socket mClientSocket;

    public ProxyServer(Socket clientSocket) {
        mClientSocket = clientSocket;
    }

    @Override
    public void run() {

    }
}
