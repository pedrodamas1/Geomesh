
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Import terrain data
df = pd.read_excel('data/disordered_points_2.xlsx').sample(10000)
print(f'This file has {len(df)} rows.')

# Bring the data closer to the origin
df = df - df.min()

# Remove rows that contain NaN values
df = df.dropna().drop_duplicates()
print(f'Number of rows afters removing NaN values: {len(df)} rows.')

# Get the data as a numpy array
x, y, z = df.to_numpy().T

# fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, color='lightpink', opacity=0.50)])
# fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, opacity=1, intensity=z, colorscale='Viridis')])
# fig.update_layout(scene = dict(aspectmode='data'))
# fig.show()

# rectangle = np.array([[0,0,500],[10,0,500],[10,10,500],[0,10,500]])

# fig = go.Figure()
# landscape = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, opacity=1, intensity=z, colorscale='Viridis')])
# module = go.Figure(data=[go.Mesh3d(x=rectangle.T[0], y=rectangle.T[1], z=rectangle.T[2], color='black')])
# fig.add_trace(landscape.data[0])
# fig.add_trace(module.data[0])
# fig.update_layout(scene = dict(aspectmode='data'))
# fig.show()
