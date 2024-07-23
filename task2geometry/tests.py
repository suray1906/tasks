import unittest
from shapes import Circle, Triangle
from utils import calculate_area, check_right_triangle

class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(check_right_triangle(triangle))

    def test_not_right_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(check_right_triangle(triangle))

if __name__ == '__main__':
    unittest.main()
