import time
import random
import sys
import base64
from Adafruit_IO import Client, Feed, RequestError
from Adafruit_IO import MQTTClient
from model_ai import *

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
    counter = counter - 1
    if counter <= 0:
        counter = 10
        # TODO
        print("Random data is publising...")
        if sensor_type == 0:    
            print("Temperature:...")
            temp = random.randint(20, 30)
            client.publish("nhietdo", temp)
            sensor_type = 1
        elif sensor_type == 1:
            print("Humidity:..")
            humi = random.randint(50, 70)
            client.publish("doam", humi)
            sensor_type = 2
        elif sensor_type == 2:
            print("Light:...")
            light = random.randint(100, 500)
            client.publish("anhsang", light)
            sensor_type = 0

    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 5
        previous_result = ai_result
        ai_result = image_detector()
        print("AI result: ", ai_result)
        if ai_result != previous_result:
            client.publish("ai", ai_result)
    time.sleep(1)
