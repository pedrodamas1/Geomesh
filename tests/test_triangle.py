import numpy as np
import unittest
from topography.triangle import Triangle

class TestTriangle(unittest.TestCase):
    def test_input_validation(self):
        # Test input validation for invalid input
        with self.assertRaises(ValueError):
            Triangle(np.array([[1, 0, 0], [0, 1, 0]]))  # Less than 3 vertices
        with self.assertRaises(ValueError):
            Triangle(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0], [1, 1, 1]]))  # More than 3 vertices

    def test_calculate_centroid(self):
        # Test centroid calculation
        vertices = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        triangle = Triangle(vertices)
        centroid = triangle.calculate_centroid()
        expected_centroid = np.array([1/3, 1/3, 0])
        np.testing.assert_array_almost_equal(centroid, expected_centroid)

    def test_calculate_area(self):
        # Test area calculation
        vertices = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        triangle = Triangle(vertices)
        area = triangle.calculate_area()
        expected_area = 0.5
        self.assertAlmostEqual(area, expected_area)

    def test_calculate_normal(self):
        # Test normal vector calculation
        vertices = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        triangle = Triangle(vertices)
        normal = triangle.calculate_normal()
        expected_normal = np.array([0, 0, 1])
        np.testing.assert_array_almost_equal(normal, expected_normal)

    def test_calculate_barycentric(self):
        # Test barycentric coordinates calculation
        vertices = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0.5]])
        triangle = Triangle(vertices)
        point = np.array([0.25, 0.25, 0.25])
        alpha, beta, gamma = triangle.calculate_barycentric(point)
        self.assertAlmostEqual(alpha + beta + gamma, 1.0)

    def test_is_coplanar(self):
        # Test coplanarity check
        vertices = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        triangle = Triangle(vertices)
        coplanar_point = np.array([1/3, 1/3, 0])  # Coplanar point
        non_coplanar_point = np.array([0.5, 0.5, 0.5])  # Non-coplanar point
        self.assertTrue(triangle.is_coplanar(coplanar_point))
        self.assertFalse(triangle.is_coplanar(non_coplanar_point))


if __name__ == '__main__':
    unittest.main()
