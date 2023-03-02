import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import rplidar

# Connect to the RPLIDAR device
lidar = rplidar.RPLidar('COM3')

# Initialize figure and plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim([-5000, 5000])
ax.set_ylim([-5000, 5000])
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')

# Add fiducial at lidar position
fiducial = plt.Circle((0, 0), 50, color='red')
ax.add_artist(fiducial)

# Initialize rotation transform
rot = transforms.Affine2D()

# Read and plot data
for scan in lidar.iter_scans():
    # Extract angles and distances from scan data
    angles = np.array([np.radians(meas[1]) for meas in scan])
    distances = np.array([meas[2] for meas in scan])
    
    # Convert polar coordinates to cartesian coordinates
    xs = distances * np.cos(angles)
    ys = distances * np.sin(angles)
    
    # Plot points in cartesian coordinates
    ax.clear()
    ax.plot(xs, ys, 'o', markersize=2)
    ax.add_artist(fiducial)  # re-add fiducial to plot
    ax.set_title('LIDAR data ({} samples)'.format(len(scan)))

     
    
    plt.pause(0.001)
    
# Close lidar connection
lidar.stop()
lidar.disconnect()

# Show plot
plt.show()
