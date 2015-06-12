
import serial
from time import sleep
ser = serial.Serial("COM11", 9600)
def connect():

    connected = False



    while not connected:
        serin = ser.read()
        connected = True

    ser.write("t")

    while ser.read() == 't':
        ser.read()
    print ("connection is ok")
    return 0


def turn_left():
    for i in range(100):
        ser.write("l")


    return 0

def turn_right():
    for i in range(130):
        ser.write("r")


    return 0


def go_forward():
    for i in range(60):
        ser.write("f")
        sleep(0.1)

    return 0

def go_backward():
    for i in range(60):
        ser.write("b")
        sleep(0.1)

    return 0

def circle_left():
    for i in range(100):
        ser.write("l")
        sleep(0.1)

    return 0

def circle_right():
    for i in range(100):
        ser.write("r")
        sleep(0.1)

    return 0

def get_angle():
    ser.write("a")
    angle=ser.read()
    return angle

def set_pid():
    ser.write("s")

connect()
while(1):
    a= raw_input()
    if a=='l':
        turn_left()
    if a=='r':
        turn_right()
    if a=='c':
        ser.close()
    if a=='s':
        set_pid()
ser.write(raw_input())
