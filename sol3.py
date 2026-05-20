"""Solution for exercise 3: custom exception and sqrt_positive."""
import math


class NegativeNumberError(Exception):
    pass


def sqrt_positive(n):
    try:
        val = float(n)
    except Exception as e:
        raise
    if val < 0:
        raise NegativeNumberError(f"Negative value: {val}")
    return math.sqrt(val)
