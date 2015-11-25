#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Install pyserial first
import serial

ser = serial.serial_for_url("/dev/cu.usbmodem1421", 9600, timeout=1)

while True:
    data = ser.readline().strip()
    if data:
        try:
            h, t, hi = map(float, data.split(","))
        except ValueError as e:
            print e
            continue
        print h, t, hi
