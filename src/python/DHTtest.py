#!/usr/bin/python
import sys
import Adafruit_DHT

while True:
    datapin = 18 # GPIO pin

    humidity, temperature = Adafruit_DHT.read_retry(11, datapin)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature,
    humidity)
