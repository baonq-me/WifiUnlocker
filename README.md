# unlockme

# 1. Configure access point mode for wlan0

## 1.1. Configure networking


## 1.2. WPA2-Personal
https://www.raspberrypi.org/documentation/configuration/wireless/access-point-routed.md

## 1.3. WPA2-Enterprise (EAP-PWD)

https://raspiblog.noblogs.org/post/2019/09/02/wpa2-enterprise-access-point-with-hostapd-and-freeradius/

# 2. Install MySQL

https://pimylifeup.com/raspberry-pi-mysql/

# 3. Install web server with PHP 7.3

https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md

# 4. Install freeradius and daloradius

https://computingforgeeks.com/install-freeradius-and-daloradius-on-debian/

## Note
/etc/freeradius/3.0/mods-enabled/eap -> uncomment "pwd" section

Run debug freeradius
```
service freeradius stop
freeradius -X
```

## Install missing packages

https://stackoverflow.com/questions/26330311/daloradius-is-not-working-db-php-file-not-found
https://stackoverflow.com/questions/4560996/call-to-undefined-function-imagecreatetruecolor-error-in-php-pchart

```
apt-get install php-mysql php-db php-gd
```

# Run python script

```
apt-get install python3-pip python3-dev python3-rpi.gpio
pip3 install gpiozero mysql.connector
```

https://raspberrypi.stackexchange.com/questions/60774/importerror-no-module-named-rpi


https://raspberrypi.stackexchange.com/questions/31663/problem-wpa-supplicant-rapsberry-pi-2/89831



http://www.binaryheartbeat.net/2013/12/raspberry-pi-based-freeradius-server.html



http://wiki.laptop.org/images/d/d7/Hostapd.conf

https://networkradius.com/doc/3.0.10/index.html
https://github.com/baonq-me/unlockme
https://gpiozero.readthedocs.io/en/stable/index.html

https://www.sendo.vn/khoa-dien-dc12v-kdc01-kem-chia-hs-16713353.html

https://www.w3schools.com/python/python_mysql_select.asp
https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html
https://stackoverflow.com/questions/2438828/mysql-datetime-to-seconds
http://lets-start-to-learn.blogspot.com/2014/08/pmksa-derivation-and-storage-in-80211i.html


https://raspberrypi.stackexchange.com/questions/37920/how-do-i-set-up-networking-wifi-static-ip-address


apt-get install hostapd dnsmasq git freeradius mariadb python3 python3-pip build-essential
