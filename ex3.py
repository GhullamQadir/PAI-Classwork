"""Exercise 3: Custom exception and validation.

Define a custom exception `NegativeNumberError` and implement `sqrt_positive(n)`
that returns the square root for non-negative numbers and raises the custom
exception for negative inputs.
"""
import math


class NegativeNumberError(Exception):
    """Raised when a negative number is provided where non-negative expected."""
    pass


def sqrt_positive(n):
    """Return sqrt(n) for n >= 0, raise NegativeNumberError for n < 0.

    Args:
        n: numeric input

    Returns:
        float: square root of n
    """
    try:
        val = float(n)
    except Exception:
        raise
    if val < 0:
        raise NegativeNumberError(f"Negative value: {val}")
    return math.sqrt(val)
