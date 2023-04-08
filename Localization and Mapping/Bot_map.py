from Class_LiDAR import LidarVisualizer
from Class_Tracker import ViveTracker
import cv2


if __name__ == '__main__':

    lidar = LidarVisualizer()
    trk = ViveTracker()
    for map_data in lidar.start():

        trk_map = trk.get_tracker_data()
        
        #convert the dimensions and channels of map_data same as trk_map....viz,. (700,450,3)
        map_data = cv2.cvtColor(map_data, cv2.COLOR_GRAY2BGR)

        #bitwise_or operation on both the images
        or_img = cv2.bitwise_or(map_data,trk_map)

        cv2.imshow('Tracker Map', or_img)
        if cv2.waitKey(1) == ord('q'):
            break
    lidar.stop()
    cv2.destroyAllWindows()