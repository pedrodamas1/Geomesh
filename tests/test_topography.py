import numpy as np
import unittest
from topography.topography import Topography

class TestTopography(unittest.TestCase):
    def setUp(self):
        # Set up test data
        self.points = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]])
        self.topography = Topography(self.points)

    def test_get_simplices(self):
        # Test get_simplices method
        simplices = self.topography.get_simplices()
        expected_simplices = np.array([[2, 3, 1], [1, 3, 0]])
        self.assertTrue(np.array_equal(simplices, expected_simplices))

    def test_get_coords(self):
        # Test get_coords method
        coords = self.topography.get_coords()
        expected_coords = np.array([[[1, 1, 0], [0, 1, 0], [1, 0, 0]],
                                   [[1, 0, 0], [0, 1, 0], [0, 0, 0]],])
        self.assertTrue(np.array_equal(coords, expected_coords))

    def test_get_triangles(self):
        # Test get_triangles method
        triangles = self.topography.get_triangles()
        self.assertEqual(len(triangles), 2)

    def test_get_centroids(self):
        # Test get_centroids method
        centroids = self.topography.get_centroids()
        expected_centroids = np.array([[2/3, 2/3, 0],
                                       [1/3, 1/3, 0],])
        np.testing.assert_allclose(centroids, expected_centroids)

    def test_get_normals(self):
        # Test get_normals method
        normals = self.topography.get_normals()
        print(normals)
        expected_normals = np.array([[0, 0, 1], [0, 0, 1]])
        np.testing.assert_allclose(normals, expected_normals)


if __name__ == '__main__':
    unittest.main()
