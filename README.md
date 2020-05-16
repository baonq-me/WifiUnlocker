# UnlockMe

# 1. Configure network

## 1.1. Connect to wifi network

Use `raspi-config`

- Connect to existing wifi network and get IP address
- Enable SSH server
- Install ssh key for root/pi user

## 1.2. Configure network interfaces

Edit file `/etc/network/interfaces`

```
# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

auto lo
iface lo inet loopback

iface eth0 inet manual

allow-hotplug wlan0
iface wlan0 inet manual

allow-hotplug wlan1
iface wlan1 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

## 1.3. Configure wpa_supplicant

Edit file `/etc/wpa_supplicant/wpa_supplicant.conf` to connect to hidden network `Baby Bone` without password authentication (my personal wifi authenticate devices via unhackable MAC address filter).

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=VN

network={
	ssid="Baby Bone"
	key_mgmt=NONE
	scan_ssid=1
}
```

Load driver `8192cu` for TP-Link TL-WN725N to work as `wlan1` by adding this line to `/etc/rc.local`

```
modprobe 8192cu
```

## 1.4. Configure dhcpcd service

Add these lines to the end of `/etc/dhcpcd.conf`

```
interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant

interface wlan1
    static ip_address=192.168.1.30/24
    static routers=192.168.1.1
    static domain_name_servers=1.1.1.1
```

## 1.5. Configure dnsmasq service

Install dnsmasq service to prodive DHCP service for client on `wlan0` network (not actually necessary).

```
apt-get install dnsmasq
```

Create new file `/etc/dnsmasq.conf`

```
interface=wlan0
dhcp-range=192.168.4.100,192.168.4.199,255.255.255.0,24h
domain=wlan
address=/gw.wlan/192.168.4.1
```

# 2. Configure access point mode for wlan0

## 2.1. WPA2-Personal

For testing purpose

https://www.raspberrypi.org/documentation/configuration/wireless/access-point-routed.md

## 2.2. WPA2-Enterprise (EAP-PWD)

Use this mode when working with `freeradius` later.

https://raspiblog.noblogs.org/post/2019/09/02/wpa2-enterprise-access-point-with-hostapd-and-freeradius/

# 3. Install LEMP stack - Linux, nginx, MySQL, PHP

Install `MariaDB` as MySQL database by following this link

https://pimylifeup.com/raspberry-pi-mysql/

Install `nginx` as a web service with PHP 7.3 by following this link

https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md

Install Linux ... oh no, we already have it :D

# 4. Install freeradius and daloradius

Install `freeradius` and `daloradius` by following this link. Remember to add an defaut RADIUS user by `daloradius`.

https://computingforgeeks.com/install-freeradius-and-daloradius-on-debian/

Enable `EAP-PWD` mode for `freeradius` by open file `/etc/freeradius/3.0/mods-enabled/eap` and uncomment `pwd` section inside `eap` section.

```
pwd {
       group = 19
       server_id = pi
       fragment_size = 1020
       virtual_server = "inner-tunnel"
}
```

Run freeradius in debugging mode when needed

```
service freeradius stop
freeradius -X
```

Install missing packages for `daloradius`

```
apt-get install php-mysql php-db php-gd
```


# 5. Run python script

Install dependencies

```
apt-get install python3-pip python3-dev python3-rpi.gpio
pip3 install gpiozero mysql.connector
```

Run file `unlockme.py` then connect to wifi network `UnlockMe` using user in `Step 4`. Debug log for `hostapd` is in syslog. Run `freeradius -X` to see debugging log in `stdout`.


# 6. References

- https://stackoverflow.com/questions/26330311/daloradius-is-not-working-db-php-file-not-found
- https://stackoverflow.com/questions/4560996/call-to-undefined-function-imagecreatetruecolor-error-in-php-pchart
- https://raspberrypi.stackexchange.com/questions/60774/importerror-no-module-named-rpi
- https://raspberrypi.stackexchange.com/questions/31663/problem-wpa-supplicant-rapsberry-pi-2/89831
- http://www.binaryheartbeat.net/2013/12/raspberry-pi-based-freeradius-server.html
- http://wiki.laptop.org/images/d/d7/Hostapd.conf
- https://networkradius.com/doc/3.0.10/index.html
- https://gpiozero.readthedocs.io/en/stable/index.html
- https://www.sendo.vn/khoa-dien-dc12v-kdc01-kem-chia-hs-16713353.html
- https://www.w3schools.com/python/python_mysql_select.asp
- https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html
- https://stackoverflow.com/questions/2438828/mysql-datetime-to-seconds
- http://lets-start-to-learn.blogspot.com/2014/08/pmksa-derivation-and-storage-in-80211i.html
- https://raspberrypi.stackexchange.com/questions/37920/how-do-i-set-up-networking-wifi-static-ip-address
