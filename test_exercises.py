import math
import os
import tempfile
import importlib

from starters import ex1, ex2, ex3


def test_safe_divide_basic():
    assert ex1.safe_divide(6, 3) == 2
    assert ex1.safe_divide(7, 2) == 3.5


def test_safe_divide_zero():
    assert ex1.safe_divide(1, 0) is None


def test_read_ints(tmp_path):
    p = tmp_path / "nums.txt"
    p.write_text("1\n2\nxyz\n3\n")
    result = ex2.read_ints(str(p))
    assert result == [1, 2, 3]

    # missing file -> empty list
    missing = tmp_path / "missing.txt"
    assert ex2.read_ints(str(missing)) == []


def test_sqrt_positive_and_negative():
    assert math.isclose(ex3.sqrt_positive(4), 2.0)
    try:
        ex3.sqrt_positive(-1)
        raised = False
    except ex3.NegativeNumberError:
        raised = True
    assert raised
