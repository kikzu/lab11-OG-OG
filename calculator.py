
# https://github.com/kikzu/lab11-OG-OG
# Partner 1: Omer Kayra Gungor
# Partner 2: Omer Kayra Gungor

import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def logarithm(a, b):
    return math.log(a, b)


def exp(a, b):
    return a ** b


def hypotenuse(a, b):
    return math.hypot(a, b)


def sqrt(a):
    return math.sqrt(a)
