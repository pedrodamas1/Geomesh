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
            
    def setUp(self):
        # Set up test data
        self.vertices = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        self.triangle = Triangle(self.vertices)

    def test_calculate_centroid(self):
        # Test calculate_centroid method
        centroid = self.triangle.calculate_centroid()
        expected_centroid = np.array([1/3, 1/3, 0])
        np.testing.assert_allclose(centroid, expected_centroid)

    def test_calculate_area(self):
        # Test calculate_area method
        area = self.triangle.calculate_area()
        expected_area = 0.5
        self.assertAlmostEqual(area, expected_area)

    def test_calculate_normal(self):
        # Test calculate_normal method
        normal = self.triangle.calculate_normal()
        expected_normal = np.array([0, 0, 1])
        np.testing.assert_allclose(normal, expected_normal)

    def test_calculate_barycentric(self):
        # Test calculate_barycentric method
        point = np.array([1/3, 1/3, 0])
        barycentric = self.triangle.calculate_barycentric(point)
        print(barycentric)
        expected_barycentric = np.array([1/3, 1/3, 1/3])
        np.testing.assert_allclose(barycentric, expected_barycentric)

    def test_is_within(self):
        # Test is_within method
        point_inside = np.array([1/3, 1/3, 0])
        point_outside = np.array([1, 1, 0])
        self.assertTrue(self.triangle.is_within(point_inside))
        self.assertFalse(self.triangle.is_within(point_outside))

    def test_calculate_interpolation(self):
        # Test calculate_interpolation method
        point = np.array([1/3, 1/3, 0])
        interpolation = self.triangle.calculate_interpolation(point)
        expected_interpolation = np.array([1/3, 1/3, 0])
        np.testing.assert_allclose(interpolation, expected_interpolation)

if __name__ == '__main__':
    unittest.main()


# class TestTriangle(unittest.TestCase):
#     def test_calculate_barycentric(self):
#         # Test barycentric coordinates calculation
#         vertices = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0.5]])
#         triangle = Triangle(vertices)
#         point = np.array([0.25, 0.25, 0.25])
#         alpha, beta, gamma = triangle.calculate_barycentric(point)
#         self.assertAlmostEqual(alpha + beta + gamma, 1.0)


