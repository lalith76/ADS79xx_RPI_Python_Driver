#!/usr/bin/python
import spidev
import time
import os
from time import sleep



spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=122000

resp=spi.xfer([0x40,0x00])#manual
resp=spi.readbytes(2)
resp=spi.readbytes(2)
resp=spi.xfer([0x2C,0x00])#auto1
resp=spi.readbytes(2)

while 1:
    for i in range(0,12):
        resp=spi.readbytes(2)
        print(str(resp)+" : CH "+str(i)+ " -> "+str(resp[1]*256+resp[0]))
    sleep(0.9)#sampling time in sec
    print("-----------------")

spi.close()
