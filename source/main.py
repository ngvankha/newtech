import time
import random
import sys
import base64
from Adafruit_IO import Client, Feed, RequestError
from Adafruit_IO import MQTTClient
#from model_ai import *
from uart import *

AIO_FEED_IDs = ["nutnhan1","nutnhan2"]
ADAFRUIT_IO_USERNAME = 'VanKha'
ADAFRUIT_IO_KEY = 'aio_LXGB270UGG9U5izyWz7nQccpT3R1'

# Kết nối tới Adafruit IO

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)


def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " tu " + feed_id)
    if feed_id == "nutnhan1":
        if payload == "0":
            writeData("1")
        else:
            writeData("2")
    if feed_id == "nutnhan2":
        if payload == "0":
            writeData("3")
        else:
            writeData("4")

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
sensor_type = 0
counter_ai = 5
ai_result = ""
previous_result = ""
while True:
   
    readSerial(client)
    time.sleep(1)
