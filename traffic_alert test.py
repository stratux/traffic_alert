#!/usr/bin/env python

from traffic_alert import traffic_alert
from audio_out import audio_out


while 1==1:
    b = int(input("bearing: (90)") or 90)
    v = int(input("vertical: (2000)") or 2000)
    m = int(input("miles: (5)") or 5)

    print(traffic_alert(b,v,m))
    audio_out(traffic_alert(b,v,m))
