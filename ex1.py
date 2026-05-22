"""Exercise 1: Safe division.

Implement `safe_divide(a, b)` to return the floating-point result of a / b.
If division by zero occurs, return `None` and do not let the exception propagate.
"""

def safe_divide(a, b):
    """Return a/b as float or None if division by zero occurs.

    Args:
        a: numerator (number)
        b: denominator (number)

    Returns:
        float result or None
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None
