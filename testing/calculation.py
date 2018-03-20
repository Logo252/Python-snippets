# -*- coding: utf-8 -*-


def add(x, y):
    """Adds numbers."""
    return x + y


def subtract(x, y):
    """Subtracts numbers."""
    return x - y


def multiply(x, y):
    """Multiplies numbers."""
    return x * y


def divide(x, y):
    """Divides numbers."""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

