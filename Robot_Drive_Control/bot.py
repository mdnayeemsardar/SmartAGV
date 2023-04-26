from motorsocketsv2 import MotorClient
import math

# Motor channels

class Bot:
    def __init__(self):
        self.mc = [2,3,0,1] # Motor channels in order m1,m2,m3,m4
        self.motor = list(map(MotorClient, self.mc))
        self.stop_val = 95  # stop value
    
    #writes a value to the specified wheel
    def move_motor(self,id, val):
        self.motor[id].write(val)

    #commands the wheels at the specified values given in list format
    def spin_motors(self, motor_values):
         for m_id,m_val in enumerate(motor_values):
            self.motor[m_id].write(m_val)

    def forward(self, speed=15):
        motor_val = [self.stop_val+speed for _ in range(len(self.mc))] #motor vel
        self.spin_motors(motor_val)
    
    def backward(self, speed=15):
        motor_val = [self.stop_val-speed for _ in range(len(self.mc))]
        self.spin_motors(motor_val)

    def right_turn(self, speed=15):
        sign = lambda motor_id : (-1)**motor_id # To get direction of motors 
        motor_val = [self.stop_val+sign(m_id)*speed for m_id in range(len(self.mc))]
        self.spin_motors(motor_val)

    def left_turn(self, speed=15):
        sign = lambda motor_id : (-1)**motor_id # To get direction of motors 
        motor_val = [self.stop_val-sign(m_id)*speed for m_id in range(len(self.mc))]
        self.spin_motors(motor_val)
    
    def stop(self):
        motor_val = [self.stop_val for _ in range(len(self.mc))]
        self.spin_motors(motor_val)

    def lat_l(self, speed=15):  #lateral left
        direct = [-1, 1, 1, -1]    # directions
        motor_val = list(map(lambda d: self.stop_val+ d*speed,direct))
        self.spin_motors(motor_val)

    def lat_r(self, speed=15):  #lateral right
        direct = [1, -1, -1, 1]    # directions
        motor_val = list(map(lambda d: self.stop_val+ d*speed,direct))
        self.spin_motors(motor_val)

    def diag_fl(self, speed=15): # front left diognal
        direct = [0, 1, 1, 0]    # directions
        motor_val = list(map(lambda d: self.stop_val+ d*speed,direct))
        self.spin_motors(motor_val)
    
    def diag_fr(self, speed=15): #front right diognal
        direct = [1, 0, 0, 1]    # directions
        motor_val = list(map(lambda d: self.stop_val+ d*speed,direct))
        self.spin_motors(motor_val)
    
    def diag_bl(self, speed=15): #back left diognal
        direct = [-1, 0, 0, -1]    # directions
        motor_val = list(map(lambda d: self.stop_val+ d*speed,direct))
        self.spin_motors(motor_val)
    
    def diag_br(self, speed=15):    # back right diognal
        direct = [0, -1, -1, 0]    # directions
        motor_val = list(map(lambda d: self.stop_val+ d*speed,direct))
        self.spin_motors(motor_val)

    def spin_cw(self, speed=15):
        motor_val = [self.stop_val + speed, self.stop_val + speed, self.stop_val - speed, self.stop_val - speed]
        self.spin_motors(motor_val)
    
    def spin_acw(self, speed=15):
        motor_val = [self.stop_val - speed, self.stop_val - speed, self.stop_val + speed, self.stop_val + speed]
        self.spin_motors(motor_val)

    def custom_direction(self, angle, speed=15):
        # Convert angle from degrees to radians
        angle_rad = math.radians(angle)
        # Calculate the motor values using trigonometry
        motor_val = [
            int(speed * math.cos(angle_rad + (2 * math.pi * i / len(self.mc))))
            for i in range(len(self.mc))
        ]
        self.spin_motors(motor_val)



    
'''    Pure rotation
    CW and CCW

    Translation along any axis'''
    

