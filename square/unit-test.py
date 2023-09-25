from square.scratch import SquareCalculations
import unittest
import math as m


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.calculation = SquareCalculations()

    def test_circul_square(self):
        for i in range(0, 100):
            eqv = round(m.pi * (i ** 2), 3)
            self.assertEqual(self.calculation.calc_square_by_side(str(i)), eqv)

    def test_rectangle_square(self):
        for i in range(0, 100):
            for j in range(0, 100):
                d = m.hypot(i, j)
                eqv = round(i * (m.sqrt((d ** 2) - (i ** 2))), 3)
                string = f'{i} {j}'
                self.assertEqual(self.calculation.calc_square_by_side(string), eqv)

    def test_right_triangle_square(self):
        for i in range(0, 100):
            for j in range(0, 100):
                k = m.hypot(i, j)
                eqv = (i * j) / 2
                string = f'{i} {j} {k}'
                self.assertEqual(self.calculation.calc_square_by_side(string), eqv)


if __name__ == "__main__":
    unittest.main()
