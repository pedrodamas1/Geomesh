import numpy as np
from scipy.spatial import Delaunay
from typing import List
from topography.triangle import Triangle
import matplotlib.pyplot as plt


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


if __name__ == '__main__':
    # Generate random points
    points = np.random.rand(5, 3)
    topography = Topography(points)

    # Plot Delaunay triangulation
    plt.triplot(points[:, 0], points[:, 1], topography.get_simplices())
    plt.plot(points[:, 0], points[:, 1], 'o')
    plt.show()
