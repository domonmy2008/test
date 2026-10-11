"""计算器模块的单元测试"""

import unittest
from calculator import add, subtract, multiply, divide, power


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


if __name__ == '__main__':
    unittest.main()
