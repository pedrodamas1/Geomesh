import numpy as np

class Triangle:
	"""
	A class to represent a triangle and perform related calculations.
	"""

	def __init__(self, coordinates: np.ndarray):
		"""
		Initialize the Triangle object with coordinates A, B, C.

		Parameters:
		coordinates (numpy.ndarray): Array of shape (3, 3) representing the vertices of the triangle.
		"""
		if not isinstance(coordinates, np.ndarray) or coordinates.shape != (3, 3):
			raise ValueError("Coordinates must be a numpy array of shape (3, 3).")
		self.coordinates = coordinates

	def __str__(self):
			"""
			Return the string representation of the Triangle object.

			Returns:
			str: String representation of the Triangle object.
			"""
			return f"Triangle(vertices={self.coordinates.tolist()})"

	def __repr__(self):
		"""
		Return the unambiguous representation of the Triangle object.

		Returns:
		str: Unambiguous representation of the Triangle object.
		"""
		return f"Triangle(coordinates={self.coordinates})"

	def calculate_centroid(self) -> np.ndarray:
		"""
		Calculate the centroid O of the triangle.

		Returns:
		numpy.ndarray: Array of shape (3,) representing the centroid coordinates.
		"""
		centroid = np.mean(self.coordinates, axis=0)
		return centroid

	def calculate_area(self) -> float:
		"""
		Calculate the area of the triangle using the cross product method.

		Returns:
		float: Area of the triangle.
		"""
		A, B, C = self.coordinates
		area = 0.5 * np.linalg.norm(np.cross(B-A, C-A))
		return area

	def calculate_normal(self, normalize: bool = False) -> np.ndarray:
		"""
		Calculate the normal vector of the triangle.

		Parameters:
		normalize (bool): If True, normalize the normal vector to unit length.

		Returns:
		numpy.ndarray: Array of shape (3,) representing the normal vector.
		"""
		A, B, C = self.coordinates
		normal = np.cross(B-A, C-A).astype(float) # Ensure normal is float array
		if normalize:
			normal /= np.linalg.norm(normal)
		return normal

	def calculate_barycentric(self, point: np.ndarray) -> np.ndarray:
		"""
		Calculate the barycentric coordinates of a point inside the triangle (projected onto the xy-plane).

		Parameters:
		point (numpy.ndarray): Array of shape (3,) representing the coordinates of the point.

		Returns:
		numpy.ndarray: Array of shape (3,) representing the barycentric coordinates (alpha, beta, gamma).
		"""
		P = point.copy()
		P[2] = 0.
		coordinates = self.coordinates.copy()
		coordinates[:,2] = 0.

		# Parse the coordinates of each vertex of the triangle
		A, B, C = coordinates
		area_ABC = Triangle( np.array([A, B, C]) ).calculate_area()

		# Calculate areas of sub-triangles
		area_APB = Triangle( np.array([A, P, B]) ).calculate_area()
		area_BPC = Triangle( np.array([B, P, C]) ).calculate_area()
		area_CPA = Triangle( np.array([C, P, A]) ).calculate_area()

		# Calculate barycentric coordinates
		alpha = area_APB / area_ABC
		beta = area_BPC / area_ABC
		gamma = area_CPA / area_ABC

		return np.array([alpha, beta, gamma])

	def is_within(self, point: np.ndarray) -> bool:
		"""
		Check if a point is within the triangle (projected onto the xy-plane).

		Parameters:
		point (numpy.ndarray): Array of shape (3,) representing the coordinates of the point.

		Returns:
		bool: Boolean value, returning True if the point is coplanar and False otherwise.
		"""
		barycentric_coordinates = self.calculate_barycentric(point)

		# Check if barycentric coordinates sum up to 1
		return np.isclose(np.sum(barycentric_coordinates), 1.0)

	def calculate_interpolation(self, point: np.ndarray) -> np.ndarray:
		"""
		Calculate the interpolation of a point within the triangle.

		Parameters:
		point (numpy.ndarray): Array of shape (3,) representing the coordinates of the point.

		Returns:
		numpy.ndarray: Interpolated coordinates.
		"""
		barycentric = self.calculate_barycentric(point)
		return np.dot(barycentric, self.coordinates)


if __name__ == '__main__':
	vertices = np.array([[0.8,-0.2,0], [0.3,1,0], [0,0,0]])
	triangle = Triangle(vertices)
	point = np.array([0.4,0.6,0])
	barycentric = triangle.calculate_barycentric(point)
	print(barycentric)

 
