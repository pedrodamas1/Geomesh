import pandas as pd
from topography.topography import Topography
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import LinearNDInterpolator

# Import terrain data
df = pd.read_excel('data/points.xlsx')
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

# Plot the figures
fig = plt.figure()

# set up the axes for the first plot
ax = fig.add_subplot(1, 2, 1, projection='3d')

# Draw the triangles of the first topography
ax.plot_trisurf(
    *topo1.points.T, 
    triangles=topo1.get_simplices(), 
    cmap=plt.cm.Spectral, alpha=1, antialiased=False)

# set up the axes for the second plot
ax = fig.add_subplot(1, 2, 2, projection='3d')

# Draw the triangles of the first topography
ax.plot_trisurf(
    *topo2.points.T, 
    triangles=topo2.get_simplices(), 
    cmap=plt.cm.Spectral, alpha=1, antialiased=False)

# Display the figure
plt.show()
