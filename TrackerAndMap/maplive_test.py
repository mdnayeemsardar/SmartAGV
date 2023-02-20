import triad_openvr
import time
import sys
from mapper import *
import cv2

v = triad_openvr.triad_openvr()
v.print_discovered_objects()

maps = Map()

if len(sys.argv) == 1:
    interval = 1/250
elif len(sys.argv) == 2:
    interval = 1/float(sys.argv[1])
else:
    print("Invalid number of arguments")
    interval = False
    
if interval:
    while(True):
        start = time.time()
        txt = ""
        for each in v.devices["tracker_1"].get_pose_euler():
            txt += "%.4f" % each
            txt += " "
        l = list(map(float, txt.split()))
        botp = np.array(l[:3]) # bot pos
        bota = l[5]             #bot orientation
        botp = botp.reshape(-1,1) 
        maps.update_bot(botp, bota)
        map_img = maps.get_map()
        cv2.imshow("Live",map_img)
        cv2.waitKey(1)
        sleep_time = interval-(time.time()-start)
        if sleep_time>0:
            time.sleep(sleep_time)