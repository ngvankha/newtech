import serial
import serial.tools.list_ports
import time

# ser = 0
# def InitSerial():
#     global ser
#     ser = serial.Serial()
#     ser.baudrate = 9600
#     ser.port = "COM4" # Port Name You want to

#     ser.timeout = 10
#     ser.open()

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    #return commPort
    return "COM4"

if getPort() != "None":
    ser = serial.Serial( port=getPort(), baudrate=115200)
    print(ser)


def processData(client, data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "T":
        client.publish("nhietdo", splitData[2])
    elif splitData[1] == "H":
        client.publish("doam", splitData[2])

mess = ""
def readSerial(client):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(client, mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

def writeData(data):
    ser.write((str(data) + "#").encode())