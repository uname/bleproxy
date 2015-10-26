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
    private static final int HEAD_SIZE = 2;
    private Socket mClientSocket;
    private InputStream mInputStream;
    private OutputStream mOutputStream;
    private OnProxyListener mListener;
    private ProtocolHandler mProtocolHandler;

    public ProxyServer(Socket clientSocket) {
        mProtocolHandler = new ProtocolHandler(this);
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
                return null;
            } finally {
                if(n < 0) {
                    LogUtil.d(TAG, "remote client closed");
                    return null;
                }
            }

            pos += n;
        }

        return buff;
    }

    public synchronized boolean send(byte[] data) {
        LogUtil.d(TAG, "send: " + StringUtil.bytesToHexString(data));
        byte[] msgBuff = new byte[HEAD_SIZE + data.length];
        msgBuff[0] = (byte) (data.length & 0x000000ff);
        msgBuff[1] = (byte) ((data.length & 0x0000ff00) >>> 8);
        System.arraycopy(data, 0, msgBuff, HEAD_SIZE, data.length);
        try {
            mOutputStream.write(msgBuff);
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }

    public int getMsgLen() {
        byte[] lenBuff = receive(HEAD_SIZE);
        if(lenBuff == null) {
            return -1;
        }
        int msgLen = (lenBuff[0] & 0xff) | ((lenBuff[1] << 8) & 0xff00);
        return msgLen;
    }

    public void stop() {
        BLEHelper.getInstance().btDisconnect("");
        try {
            mClientSocket.close();
            // TODO: disconnect ble
        } catch (IOException e) {
            e.printStackTrace();
        }
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
