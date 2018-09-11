from math import sqrt


def f(x):
    return 7 * (x ** 2) + (2 * x)


def g(x, y):
    return (x ** 2) + (y ** 2)


def hypotenuse(x, y):
    return sqrt((x ** 2) + (y ** 2))


def is_positive(x):
    return x > 0
