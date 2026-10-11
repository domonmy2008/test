"""简单的计算器模块

这个模块提供基本的数学运算功能。
"""


def add(a, b):
    """加法运算"""
    return a + b


def subtract(a, b):
    """减法运算"""
    return a - b


def multiply(a, b):
    """乘法运算"""
    return a * b


def divide(a, b):
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def power(a, b):
    """幂运算"""
    return a ** b
