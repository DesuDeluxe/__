import serial

https://github.com/DesuDeluxe/oop/new/master#fullscreen
connected = False

ser = serial.Serial("COM11", 9600)


while not connected:
    serin = ser.read()
    connected = True


ser.write("l")


while ser.read() == 'l':
    ser.read()

ser.close()
