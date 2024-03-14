import pandas as pd
from topography.topography import Topography
import matplotlib.pyplot as plt

# Import terrain data
df = pd.read_excel('data/disordered_points.xlsx')
print(f'This file has {len(df)} rows.')

# Remove duplicates
df = df.drop_duplicates()
print(f'Number of rows afters removing duplicates: {len(df)} rows.')

# Bring the data closer to the origin
df = df - df.min()

# Get a sample from the dataframe
# df = df.sample(500)
# df = df[:100]

# Get the data as a numpy array
points = df.to_numpy()

# Create the topography object
topo1 = Topography(points)

# Create the grid interpolation topography
topo2 = topo1.interpolate(50)

# Save the ordered terrain
topo2.save('data/ordered_points.xlsx')

# Plot the figures
fig = plt.figure()

# set up the axes for the first plot
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Draw the triangles of the first topography
ax1.plot_trisurf(
    *topo1.points.T, 
    triangles=topo1.get_simplices(), 
    cmap=plt.cm.Spectral, alpha=1, antialiased=False)

# set up the axes for the second plot
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# Draw the triangles of the first topography
ax2.plot_trisurf(
    *topo2.points.T, 
    triangles=topo2.get_simplices(), 
    cmap=plt.cm.Spectral, alpha=1, antialiased=False)

# Display the figure
ax1.set_aspect('equal')
ax2.set_aspect('equal')
plt.show()
