"""Solution for exercise 1: safe_divide."""

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
