from rplidar import RPLidar
import time
import pandas as pd
import keyboard 

# Initialize RP Lidar
lidar = RPLidar('COM3')

# Create empty DataFrame to store data
data = pd.DataFrame(columns=['Distance', 'Angle'])

# Start scanning loop
for scan in lidar.iter_scans():

    # Extract distance and angle data from scan
    distances = [measurement[2] for measurement in scan]
    angles = [measurement[1] for measurement in scan]

    # Create DataFrame with scan data
    scan_data = pd.DataFrame({'Distance': distances, 'Angle': angles})

    # Add scan data to main DataFrame
    data = pd.concat([data, scan_data], ignore_index=True)

    # Wait a short time before starting next scan
    time.sleep(0.1)

    # Break out of loop after a certain number of scans (optional)
    if keyboard.is_pressed('Esc'):
        print("Exiting loop...")
        break

# Stop RP Lidar
lidar.stop()
lidar.disconnect()

# Save data to Excel file
filename = 'lidar_data_1.xlsx'
data.to_excel(filename, index=False)
