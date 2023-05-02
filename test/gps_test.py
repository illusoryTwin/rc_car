import serial
import time
import string 
import pynmea2

port="/dev/ttyUSB0"
ser=serial.Serial(port,baudrate=9600,timeout=0.5)


try:
    while True: 
        dataout =pynmea2.NMEAStreamReader()
        newdata=ser.readline().decode('utf-8')
        print(newdata)
        # print(pynmea2.parse(newdata))
        # newdata[0:6]
        if newdata[0:6]=='$GNGGA':

            # newmsg=pynmea2.parse(newdata)
            print(newdata.split(','))
            # lat=newmsg.latitude

            # lng=newmsg.longitude
            # print(lat, lng)

        # gps=“Latitude=" +str(lat) + “and Longitude=" +str(lng)

except KeyboardInterrupt:
    print('Exit....')
finally:
    ser.close()