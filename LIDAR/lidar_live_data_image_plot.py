import cv2
import numpy as np
from rplidar import RPLidar

# Initialize the LIDAR object
lidar = RPLidar('COM3')

# Set the image resolution and dimensions
resolution = 10  # 10 mm per pixel
width = 640      # 640 pixels in the x-axis
height = 480     # 480 pixels in the y-axis

# Create a blank image with NumPy
image = np.zeros((height, width), dtype=np.uint8)

# Start the LIDAR motor and begin scanning
lidar.start_motor()

# Loop indefinitely and continuously update the image
for scan in lidar.iter_scans():
    # Reset the image to all zeros
    image.fill(0)

    # Loop through each scan and populate the image
    for (_, angle, distance) in scan:
        print("Distance: ", distance, " angle: ",angle )
        x = int(distance * np.sin(np.radians(angle)) / resolution + width // 2)
        y = int(distance * np.cos(np.radians(angle)) / resolution + height // 2)
        if 0 <= x < width and 0 <= y < height:
            image[y, x] = 255

    # Mark the LIDAR position with a triangular fiducial
    cv2.drawMarker(image, (width // 2, height // 2), (255, 0, 0), cv2.MARKER_TRIANGLE_UP, markerSize=10, thickness=2)

    # Show the image with the LIDAR data in real-time
    cv2.imshow('LIDAR Data', image)
    if cv2.waitKey(1) == 27:  # Press Esc key to exit the loop
        break

# Stop the LIDAR motor
lidar.stop_motor()

# Close the OpenCV window and release resources
cv2.destroyAllWindows()
