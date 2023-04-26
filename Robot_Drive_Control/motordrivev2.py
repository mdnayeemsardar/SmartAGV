from adafruit_servokit import ServoKit


class MotorDrive:
    def __init__(self, kit):
        self.kit = kit                      
        self.pd = [95 for _ in range(4)]       #previous command for all motors

    def set_range(self, channels):              #set range of pulse 
        for channel in channels:
            self.kit.servo[channel].set_pulse_width_range(1000, 2000) #1000-2000 is pwmrange in rc mode for sabertooth
            
    def  clip(self, val, minVal = 0, maxVal = 180): # clip the values to range of writable values ( 0 to 180 )
        val = int(val)
        return max(min(maxVal,val), minVal)

    def write(self, channel=0, val = 95):     #95 is stop  0-100 is reverse 100-180 is forward     
        if val != self.pd[channel]:
            self.kit.servo[channel].angle = self.clip(val) #writing value to motors
            self.pd[channel] = val                                 