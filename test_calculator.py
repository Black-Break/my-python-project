"""test_calculator.py —— calculator 模块的单元测试。

使用 pytest 运行:
    pytest -v
"""

import pytest

from calculator import add, subtract, multiply, divide, power


# ---------- add ----------

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_add_more_cases():
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    assert add(-2, -3) == -5


# ---------- subtract ----------

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(7, 0) == 7


# ---------- multiply ----------

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(2, 0) == 0


def test_multiply_negative():
    assert multiply(-3, 4) == -12
    assert multiply(-3, -4) == 12


# ---------- divide ----------

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


# ---------- power ----------

def test_power():
    assert power(2, 10) == 1024
    assert power(5, 0) == 1
    assert power(-2, 3) == -8