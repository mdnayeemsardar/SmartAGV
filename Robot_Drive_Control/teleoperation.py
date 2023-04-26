from bot import *

agv = Bot()

trottle = 35 # 0 < trottle < 80 
print("Joystic mode LIVE !")
while True:
    cmd = input("Command :")
    if cmd == 'w':
        agv.forward(trottle)
    elif cmd == 's':
        agv.backward(trottle)
    elif cmd == 'a':
        agv.left_turn(trottle)
    elif cmd == 'd':
        agv.right_turn(trottle)
    elif cmd == 'u':
        trottle+=5
        print("Trottle -> {}".format(trottle))
    elif cmd == 'j':
        trottle-=5
        print("Trottle -> {}".format(trottle))
    elif cmd == 'q':
        agv.lat_l(trottle)
    elif cmd == 'e':
        agv.lat_r(trottle)
    elif cmd == 't':
        agv.diag_fl(trottle)
    elif cmd == 'y':
        agv.diag_fr(trottle)
    elif cmd == 'g':
        agv.diag_bl(trottle)
    elif cmd == 'h':
        agv.diag_br(trottle)
    elif cmd == 'l':
        agv.spin_cw(trottle)
    elif cmd == 'p':
        agv.spin_acw(trottle)
    elif cmd == 'custom':
        angle = input("angle :")
        angle = int(angle)
        agv.custom_direction(angle, trottle)
    else:
        agv.stop()

