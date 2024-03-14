import numpy as np
import pandas as pd
from typing import List
from topography.triangle import Triangle
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
from scipy.interpolate import LinearNDInterpolator

class Topography:
    """
    A class to represent topographical data and perform related calculations.
    """

    def __init__(self, points: np.ndarray) -> None:
        """
        Initialize the Topography object with points.

        Parameters:
        points (numpy.ndarray): Array representing the points in 3D space.
        """
        self.points = points
        self.triangulation = Delaunay(points[:, :2])

    def get_simplices(self) -> np.ndarray:
        """
        Get the simplices of the Delaunay triangulation.

        Returns:
        numpy.ndarray: Array of shape (N, 3) representing the simplices.
        """
        return self.triangulation.simplices

    def get_coords(self) -> np.ndarray:
        """
        Get the coordinates of the simplices.

        Returns:
        numpy.ndarray: Array of shape (N, 3, 3) representing the coordinates of the simplices.
        """
        simplices = self.get_simplices()
        return self.points[simplices]

    def get_triangles(self) -> List[Triangle]:
        """
        Get the list of Triangle objects corresponding to the simplices.

        Returns:
        List[Triangle]: List of Triangle objects.
        """
        coords = self.get_coords()
        return [Triangle(coord) for coord in coords]

    def get_centroids(self) -> np.ndarray:
        """
        Calculate the centroids of the triangles.

        Returns:
        numpy.ndarray: Array of shape (N, 3) representing the centroids of the triangles.
        """
        triangles = self.get_triangles()
        return np.array([triangle.calculate_centroid() for triangle in triangles])

    def get_normals(self) -> np.ndarray:
        """
        Calculate the normals of the triangles.

        Returns:
        numpy.ndarray: Array of shape (N, 3) representing the normals of the triangles.
        """
        triangles = self.get_triangles()
        return np.array([triangle.calculate_normal(normalize=True) for triangle in triangles])

    def interpolate(self, N: int) -> np.ndarray:
        """
        Linear interpolator.

        Parameters:
        N (int): Number of grid steps.

        Returns:
        Topography: Topography object with the interpolated points.
        """
        x, y, z = self.points.T
        X = np.linspace(min(x), max(x), N)
        Y = np.linspace(min(y), max(y), N)
        X, Y = np.meshgrid(X, Y)

        interp = LinearNDInterpolator(list(zip(x, y)), z)
        Z = interp(X, Y)
        points = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T
        return Topography(points)

    def save(self, path: str) -> None:
        """
        Save the points to an excel file.

        Parameters:
        path (str): path with directory and name of file to save.

        Returns:
        None
        """
        df = pd.DataFrame(self.points, columns=['x', 'y', 'z'])
        df.to_excel(path, index=False)
        return None


if __name__ == '__main__':
    # Generate random points
    points = np.array([[1,0,0],[0,1,0],[0,0,1]])
    topography = Topography(points)

    # Plot Delaunay triangulation
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    # Draw the triangles
    ax.plot_trisurf(
        *topography.points.T, 
        triangles=topography.get_simplices(), 
        cmap=plt.cm.Spectral, alpha=0.5)

    # Draw the triangle vertices
    ax.scatter(*topography.points.T)

    # Draw the normal vectors
    ax.scatter(*topography.get_centroids().T)
    ax.quiver(*topography.get_centroids().T, *topography.get_normals().T)

    # Draw some interpolated point for verification
    point = np.array([1/3,1/5,0])
    triangle = topography.get_triangles()[0]
    interp = triangle.calculate_interpolation(point)
    ax.scatter(*interp)
    
    # Display the plots
    ax.set_title('Feature visualization of a triangle')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_aspect('equal')
    plt.show()