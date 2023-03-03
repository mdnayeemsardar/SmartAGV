import pandas as pd
import numpy as np
import cv2

# read the data from the Excel file
data = pd.read_excel('lidar_data_1.xlsx', names=['distance', 'angle'])

# convert angles from degrees to radians
angles = data['angle'] * (2 * 3.14159) / 360

# set the image size and resolution
resolution = 10  # 1 pixel = 10 mm
width = int(4500 / resolution)  # 20000 mm = 20 m
height = int(7000 / resolution)  # 20000 mm = 20 m

# create a blank image
image = np.zeros((height, width), dtype=np.uint8)

# populate the image with LIDAR data
for i in range(len(data)):
    x = int(data.iloc[i]['distance'] * pd.np.sin(angles[i]) / resolution + width // 2)
    y = int(data.iloc[i]['distance'] * pd.np.cos(angles[i]) / resolution + height // 2)
    if 0 <= x < width and 0 <= y < height:
        image[y, x] = 255

# plot the image
cv2.imshow('LIDAR Data', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
