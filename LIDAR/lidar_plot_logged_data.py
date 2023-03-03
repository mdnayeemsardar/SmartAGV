import pandas as pd
import matplotlib.pyplot as plt

# read the data from the Excel file
data = pd.read_excel('lidar_data_1.xlsx', names=['distance', 'angle'])

# convert angles from degrees to radians
angles = data['angle'] * (2 * 3.14159) / 360

# plot the LIDAR data in Cartesian coordinates
plt.scatter(data['distance'] * pd.np.sin(angles), data['distance'] * pd.np.cos(angles), marker='.', linestyle='None')

# plot a marker to indicate the position of the LIDAR
plt.plot(0, 0, marker='o', markersize=10, color='red')

# add labels and title
plt.title('LIDAR Data')
plt.xlabel('X distance (meters)')
plt.ylabel('Y distance (meters)')

# show the plot
plt.show()
