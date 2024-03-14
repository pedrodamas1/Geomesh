
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.interpolate import LinearNDInterpolator

# Create the figure for the scene
fig = go.Figure()

# Import terrain data
df = pd.read_excel('data/disordered_points_2.xlsx').sample(5000)
print(f'This file has {len(df)} rows.')

# Bring the data closer to the origin
df = df - df.min()

# Remove rows that contain NaN values
df = df.dropna().drop_duplicates()
print(f'Number of rows afters removing NaN values: {len(df)} rows.')

# Get the data as a numpy array
points = df.to_numpy()

# Add the terrain to the scene
landscape = go.Figure(data=[go.Mesh3d(x=points.T[0], y=points.T[1], z=points.T[2], opacity=1, intensity=points.T[2], colorscale='Viridis')])
fig.add_trace(landscape.data[0])

# Create the 2D interpolator for placing the pannels
interp = LinearNDInterpolator(list(zip(points.T[0], points.T[1])), points.T[2])

# Create the 2D values for the inerpolation
x = np.arange(400, 800, 50)
y = np.arange(400, 800, 15)
X, Y = np.meshgrid(x, y)
Z = interp(X, Y)

# Compile the output into a list of points
points = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T

# Create a template for each module
rectangle = np.array([[0,0,10],[20,0,10],[20,10,10],[0,10,10]])

# Loop over all module points
for point in points:
    coords = rectangle + point

    # Add the module to the scene
    module = go.Figure(data=[go.Mesh3d(x=coords.T[0], y=coords.T[1], z=coords.T[2], color='black', opacity=0.9)])
    fig.add_trace(module.data[0])

# Show the scene
fig.update_layout(scene = dict(aspectmode='data'))
fig.show()
