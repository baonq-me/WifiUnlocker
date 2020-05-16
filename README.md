# unlockme

# Config access point mode for wlan0

## WPA2-Personal
https://www.raspberrypi.org/documentation/configuration/wireless/access-point-routed.md

## WPA2-Enterprise (EAP-PWD)

https://raspiblog.noblogs.org/post/2019/09/02/wpa2-enterprise-access-point-with-hostapd-and-freeradius/

# Install MySQL

https://pimylifeup.com/raspberry-pi-mysql/

# Install web server with PHP 7.3

https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md

# Install freeradius

https://computingforgeeks.com/install-freeradius-and-daloradius-on-debian/
(missing package php7.3-mysql)

/etc/freeradius/3.0/mods-enabled/eap -> uncomment "pwd" section

Run debug freeradius
```
service freeradius stop
freeradius -X
```


https://raspberrypi.stackexchange.com/questions/31663/problem-wpa-supplicant-rapsberry-pi-2/89831



http://www.binaryheartbeat.net/2013/12/raspberry-pi-based-freeradius-server.html

https://stackoverflow.com/questions/26330311/daloradius-is-not-working-db-php-file-not-found

https://stackoverflow.com/questions/4560996/call-to-undefined-function-imagecreatetruecolor-error-in-php-pchart

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
