from motorsocketsv2 import MotorServer
import Jetson.GPIO as GPIO
from adafruit_servokit import ServoKit
from motordrivev2 import MotorDrive
import busio
import board

# Motor channels
M1C = 2 
M2C = 3
M3C = 0
M4C = 1

def log(msg):
    print(msg)


log("Drive unit status -> STARTING ..")

i2c_bus0=(busio.I2C(board.SCL_1, board.SDA_1))
pca9685 = ServoKit(channels = 16, i2c=i2c_bus0)

dport = MotorServer()   # data port
mcu = MotorDrive(pca9685)   # motor control unit  

mcu.set_range([M1C, M2C, M3C, M4C]) # Set pulse ranges
log("Drive unit status -> READY !!")

while True:
    mid, value = dport.recv()
    log("Data : " + " ".join(map(str,[mid,value])))
    if mid is not None:
        mcu.write(mid, value)