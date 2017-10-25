#!/usr/bin/env python

import websocket
import json
import threading
from time import sleep


def on_situation_message(ws, message):
	situationData = json.loads(message)
	print("### new situation data ###")
	print("BaroPressureAltitude: {}".format(situationData["BaroPressureAltitude"]))

def on_traffic_message(ws, message):
	trafficData = json.loads(message)
	print("### new traffic data ###")
	print("BearingDist_valid: {}".format(trafficData["BearingDist_valid"]))
	print("Bearing: {}".format(trafficData["Bearing"]))
	print("Distance: {}".format(trafficData["Distance"]))
	print("Alt: {}".format(trafficData["Alt"]))

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
	print("### opened ###")


if __name__ == "__main__":
	# Traffic updates websocket.
    ws_traffic = websocket.WebSocketApp("ws://localhost/traffic",
                              on_message = on_traffic_message,
                              on_error = on_error,
                              on_close = on_close)
    wst = threading.Thread(target=ws_traffic.run_forever)
    wst.daemon = True
    wst.start()
    # Situation (ownship) websocket.
    ws_situation = websocket.WebSocketApp("ws://localhost/situation",
                              on_message = on_situation_message,
                              on_error = on_error,
                              on_close = on_close)
    ws_situation.on_open = on_open
    ws_situation.run_forever()

