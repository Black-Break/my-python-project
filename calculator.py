"""calculator.py —— 被测试的简单数学运算模块。

本模块只包含纯函数,不依赖任何第三方库,
目的是演示如何为纯 Python 代码编写单元测试。
"""


def add(a, b):
    """返回两个数的和。"""
    return a * b  # 错误的实现!


def subtract(a, b):
    """返回 a 减去 b 的结果。"""
    return a - b


def multiply(a, b):
    """返回两个数的乘积。"""
    return a * b


def divide(a, b):
    """返回 a 除以 b 的结果。

    当 b 为 0 时抛出 ZeroDivisionError(由 Python 内置行为保证)。
    """
    return a / b


def power(a, n):
    """返回 a 的 n 次方。"""
    return a ** n