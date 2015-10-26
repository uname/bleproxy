package com.hqw.bleproxy.net;

import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.util.Enumeration;
import java.util.Locale;

/**
 * Created by Administrator on 2015/10/26.
 */
public class NetUtil {

    public static String getLocalIpAddress() throws SocketException
    {
        String ipv4 = null;
        for(Enumeration<NetworkInterface> en = NetworkInterface.getNetworkInterfaces(); en.hasMoreElements(); )
        {
            NetworkInterface intf = en.nextElement();
            if(!intf.getName().toLowerCase(Locale.getDefault()).equals("wlan0")) {
                continue;
            }
            for(Enumeration<InetAddress> enumIpAddr = intf.getInetAddresses(); enumIpAddr.hasMoreElements(); )
            {
                InetAddress inetAddress = enumIpAddr.nextElement();
                if(!inetAddress.isLoopbackAddress() && (inetAddress instanceof Inet4Address))
                {
                    ipv4 = inetAddress.getHostAddress().toString();
                }
            }
        }

        return ipv4;
    }
}
