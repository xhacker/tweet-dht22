#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import timedelta
from datetime import datetime

# Install pyserial
import serial

# Install python-twitter
import twitter

ser = serial.serial_for_url("/dev/cu.usbmodem1421", 9600, timeout=1)

api = twitter.Api(
    consumer_key="consumer_key",
    consumer_secret="consumer_secret",
    access_token_key="access_token",
    access_token_secret="access_token_secret")

tweet_interval = timedelta(minutes=15)
last_post = None

while True:
    data = ser.readline().strip()
    if data:
        try:
            h, t, hi = map(float, data.split(","))
        except ValueError as e:
            print e
            continue

        status = "Temperature: {}℃ \nHumidity: {}% \nHeat Index: {}℃".format(h, t, hi)
        print status
        print "\n"
        if (not last_post) or (datetime.now() - last_post > tweet_interval):
            api.PostUpdate(status)
            last_post = datetime.now()
