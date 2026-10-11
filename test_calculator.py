"""计算器模块的单元测试"""

import unittest
from calculator import add, subtract, multiply, divide, power, modulo, sqrt


class TestCalculator(unittest.TestCase):
    """计算器功能测试类"""

    def test_add(self):
        """测试加法"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """测试减法"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(10, 10), 0)

    def test_multiply(self):
        """测试乘法"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        """测试除法"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """测试除零异常"""
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        """测试幂运算"""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(10, 2), 100)

    def test_modulo(self):
        """测试模运算"""
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(15, 5), 0)
        self.assertEqual(modulo(7, 4), 3)
        self.assertEqual(modulo(20, 6), 2)

    def test_modulo_by_zero(self):
        """测试模运算除零异常"""
        with self.assertRaises(ValueError):
            modulo(10, 0)

    def test_sqrt(self):
        """测试平方根运算"""
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(0), 0)
        self.assertAlmostEqual(sqrt(2), 1.4142135623730951)
        self.assertEqual(sqrt(16), 4)

    def test_sqrt_negative(self):
        """测试负数平方根异常"""
        with self.assertRaises(ValueError):
            sqrt(-1)
        with self.assertRaises(ValueError):
            sqrt(-10)


if __name__ == '__main__':
    unittest.main()
