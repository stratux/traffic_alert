#!/usr/bin/env python

import math
from math import atan, degrees
 
#convert ft to nm
FT2NM = 0.0001645784

#possible configuration values
high_angle = 15 # degrees
low_angle = -15 # degrees

def traffic_alert(bearing, vertical, distance):
    """Generate audio alert string
    """
    #  bearing is relative to heading (-180 :: +180)
    # vertical: feet +- relative to ship
    # distance in nm
    
    if bearing > 0:
        oclock = int((bearing + 15) / 30)
    else:
        oclock = 12 + int((bearing - 15) / 30)
    if oclock == 0:
        oclock = 12
        
    #calcuate visual angle
    angle = math.degrees(math.atan(vertical*FT2NM/distance))
    visual_angle = ""
    if angle < low_angle:
        visual_angle = "low "
    elif angle > high_angle:
        visual_angle = "high "
    
    return ("traffic " + str(oclock) + " oh clock " + visual_angle + str(int(distance))
            + " mile"+[" ","s, "][int(distance)>1])

