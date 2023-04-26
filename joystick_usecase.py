import pygame
from scipy.interpolate import interp1d
from bot import *

agv = Bot()

trottle = 35 # 0 < trottle < 80 
print("Joystic mode LIVE !")

# Initialize pygame and the game controller
pygame.init()
pygame.joystick.init()

# Get the number of available game controllers
num_joysticks = pygame.joystick.get_count()

# If no game controller is found, print an error message and exit
if num_joysticks == 0:
    print("No game controller found.")
    pygame.quit()
    exit()

# Get the first game controller in the list
gamepad = pygame.joystick.Joystick(0)
gamepad.init()

# Main loop
while True:
    # Get the latest events from pygame
    events = pygame.event.get()

    # Check each event
    for event in events:
        # If the event is a button press or release
        if event.type == pygame.JOYBUTTONDOWN:
            # Get the button that was pressed or released
            button = event.button


            if button == 0:
                # Send a command to the robot to move forward
                # For example, you could use the PySerial library to send the command over serial
                #print("You pressed A")
                trottle+=5
                print("Trottle -> {}".format(trottle))

            if button == 1:
                #print('You pressed B')
                trottle-=5
                print("Trottle -> {}".format(trottle))
                
            if button == 2:

                print('You pressed X')
                
            if button == 3:

                print('You pressed Y')

            if button == 4:

                print('You pressed LB')

            if button == 5:

                print('You pressed RB')

            if button == 6:

                print('You pressed back button')

            if button == 7:

                print('You pressed Start')

            if button == 8:

                print('You pin pushed left joystick')

            if button == 9:

                print('You pin pushed right joystick')



        # If the event is an axis motion
        elif event.type == pygame.JOYAXISMOTION:
            # Get the axis that was moved and its current value
            axis = event.axis
            value = event.value
            if(value<-1 or value>1):
                continue

            #print(type(value))
            speed = interp1d([-1,1] ,[-80, 80])
            s = speed(value)

            # If the axis is the left joystick Y axis
            if axis == 0:
                # Send a command to the robot to move based on the joystick position
                # For example, you could use the PySerial library to send the command over serial
                print("left/right movement with Left Joystick", s)

            if axis == 1:
                # Send a command to the robot to move based on the joystick position
                # For example, you could use the PySerial library to send the command over serial

                print("forward/backward movement with Left Joystick", s)
                


            if axis == 2:
                # Send a command to the robot to move based on the joystick position
                # For example, you could use the PySerial library to send the command over serial

                print("left/right movement with Right Joystick", s)


            if axis == 3:
                # Send a command to the robot to move based on the joystick position
                # For example, you could use the PySerial library to send the command over serial

                print("forward/backward movement with Right Joystick", s)

            if axis == 4:
                # Send a command to the robot to move based on the joystick position
                # For example, you could use the PySerial library to send the command over serial

                print("pressing LT button", s)
 

            if axis == 5:
                # Send a command to the robot to move based on the joystick position
                # For example, you could use the PySerial library to send the command over serial

                print("pressing RT button", s)
  



    # Wait a short amount of time before checking for events again
    pygame.time.wait(10)

'''
from scipy.interpolate import interp1d
>>> m = interp1d([-1.000,1.000],[-80, 80])
>>> m(256)
array(7.4951076320939336)

'''