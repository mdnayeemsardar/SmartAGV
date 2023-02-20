from turtle import color
import roboticstoolbox
from spatialmath.base import *
import numpy as np
import cv2

class Map:
    def __init__(self,floor_w = 7000, floor_h=8000, resolution = 10,
                    y_rotation=-37, z_rotation=180, x_translation=6):
        self.imgh = int(floor_h/resolution) #map image heigh
        self.imgw = int(floor_w/resolution) #map image width
        self.resolution = resolution
        self.room_map = np.zeros((self.imgh,self.imgw,3), dtype=np.uint8)
        self.map = self.room_map.copy()
        self.rot_y = roty(y_rotation)
        self.rot_z = rotz(z_rotation)
        self.trans_x = [[x_translation],
                                    [0],
                                    [0]]
        self.bot_pos = (int(self.imgh/2), int(self.imgw/2))

    def tracker2map(self, tracker_xyz, theta): #tracker xyz is a 3x1 matrix
        p = np.dot(self.rot_y, tracker_xyz)
        p = np.dot(self.rot_z, p)
        p = np.add(p,self.trans_x)
        print(p, end="  ")
        img_c = int((abs(p[0][0])*1000)/self.resolution)
        img_r = int((abs(p[2][0])*1000)/self.resolution)

        return img_r, img_c
    
    def bot_marker(self):
        r, c = self.bot_pos[0], self.bot_pos[1]
        fed = np.array([    [r, c],
                       [r+5, c-10],
                        [r-15,  c],
                        [r+5,c+10],
                            [r, c]],)
        return fed
    
    def update_bot(self, t_xyz,t_theta):
        self.bot_pos = tuple(self.tracker2map(t_xyz, t_theta))
        print(self.bot_pos)

    def update_map(self):
        self.map = self.room_map.copy()
        self.map = cv2.fillPoly(self.map, [self.bot_marker()], color = (0,69,255))
    def get_map(self):
        self.update_map()
        return self.map


    



