import unittest
from geometry_calculator import circle_area, triangle_area, is_right_triangle, get_shape_area, math

class TestGeometryCalculator(unittest.TestCase):

    def test_circle_area(self):
        self.assertEqual(circle_area(1), math.pi)
        self.assertEqual(circle_area(2), 4 * math.pi)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(3, 4, 5), 6)

    def test_is_right_triangle(self):
        self.assertTrue(is_right_triangle(3, 4, 5))
        self.assertFalse(is_right_triangle(3, 4, 6))

    def test_get_shape_area(self):
        self.assertEqual(get_shape_area(1), math.pi)
        self.assertEqual(get_shape_area(3, 4, 5), 6)

if __name__ == '__main__':
    unittest.main()
