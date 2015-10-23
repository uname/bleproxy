package com.hqw.bleproxy.net;

import com.hqw.bleproxy.LogUtil;
import com.hqw.bleproxy.StringUtil;
import com.hqw.bleproxy.BLEHelper;
import com.hqw.bleproxy.protocol.ProtocolHandler;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

/**
 * Created by Administrator on 2015/10/22.
 */
public class ProxyServer implements Runnable {

    private static final String TAG = ProxyServer.class.getSimpleName();
    private Socket mClientSocket;
    private InputStream mInputStream;
    private OutputStream mOutputStream;
    private OnProxyListener mListener;
    private ProtocolHandler mProtocolHandler;

    public ProxyServer(Socket clientSocket) {
        mProtocolHandler = new ProtocolHandler();
        mClientSocket = clientSocket;
        try {
            mInputStream = clientSocket.getInputStream();
            mOutputStream = clientSocket.getOutputStream();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public interface OnProxyListener {
        void clientDisconnected(ProxyServer proxyServer);
    }

    public void setOnProxyListener(OnProxyListener listener) {
        mListener = listener;
    }

    private byte[] receive(int len) {
        byte[] buff = new byte[len];
        int n = 0;
        int pos = 0;

        while(pos < len) {
            try {
                n = mInputStream.read(buff, pos, len - pos);
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                if(n < 0) {
                    LogUtil.e(TAG, "socket closed");
                    return null;
                }
            }
            pos += n;
        }

        return buff;
    }

    public int getMsgLen() {
        byte[] lenBuff = receive(2);
        if(lenBuff == null) {
            return -1;
        }
        int msgLen = (lenBuff[0] & 0xff) | ((lenBuff[1] << 8) & 0xff00);
        return msgLen;
    }

    @Override
    public void run() {

        while (true) {
            int msgLen = getMsgLen();
            LogUtil.d(TAG, "msgLen is " + msgLen);
            if(msgLen < 0) {
                break;
            }
            byte[] msgBuff = receive(msgLen);
            if(msgBuff == null) {
                break;
            }
            LogUtil.d(TAG, "msgBuff: " + StringUtil.bytesToHexString(msgBuff));
            mProtocolHandler.handleMsg(msgBuff);
        }


        try {
            mClientSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        if(mListener != null) {
            mListener.clientDisconnected(this);
        }
    }
}
