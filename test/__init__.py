from io import StringIO
import sys
import unittest

def calculate_expression(s, a, b):
    result = None
    if s == '+':
        result = a + b
    elif s == '-':
        result = a - b
    elif s == '*':
        result = a * b
    elif s == '/':
        if b != 0:
            result = a / b
        else:
            return 'Деление на ноль!'
    return result

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_addition(self):
        self.assertEqual(calculate_expression('+', 5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(calculate_expression('-', 5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(calculate_expression('*', 5, 3), 15)

    def test_division(self):
        self.assertEqual(calculate_expression('/', 6, 3), 2)
        self.assertEqual(calculate_expression('/', 5, 0), 'Деление на ноль!')

if __name__ == '__main__':
    unittest.main()
