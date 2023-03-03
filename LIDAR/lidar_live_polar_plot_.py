import numpy as np
import matplotlib.pyplot as plt
import rplidar

# Connect to the RPLIDAR device
lidar = rplidar.RPLidar('COM3')

# Initialize figure and plot
fig, ax = plt.subplots(subplot_kw=dict(polar=True))
ax.set_rmax(5000)
ax.grid(True)

# Read and plot data
for scan in lidar.iter_scans():
    # Extract angles and distances from scan data
    angles = np.array([np.radians(meas[1]) for meas in scan])
    distances = np.array([meas[2] for meas in scan])
    
    # Plot points in polar coordinates
    ax.plot(angles, distances, 'o', markersize=2)
    plt.pause(0.001)
    
    # Clear plot for next scan
    ax.clear()

# Close lidar connection
lidar.stop()
lidar.disconnect()

# Show plot
plt.show()
