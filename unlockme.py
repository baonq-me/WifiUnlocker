#!/usr/bin/python

from gpiozero import LED
import mysql.connector
from time import sleep

mydb = mysql.connector.connect(
  host="localhost",
  user="freeradius",
  passwd="radius@2",
  database="freeradius"
)

print("Connected to MySQL !")

relay = LED(17)

mycursor = mydb.cursor()

while True:
    mycursor.execute("select * from radpostauth where reply = 'Access-Accept' and authdate > (now() - 3);")
    myresult = mycursor.fetchall()

    if len(myresult) > 0:
         for x in myresult:
              print(x)
         relay.on()
         sleep(5)
         relay.off()

    sleep(3)
