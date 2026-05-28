Lab: Exception Handling in Python
================================

Course: Programming for AI (2+0)
Topic: Exception handling in Python

Overview
--------
This lab introduces Python exceptions: built-in exceptions, try/except/else/finally, raising exceptions, and creating custom exceptions. Students will complete three progressive exercises with starter code, run tests, and compare with provided solutions.

Learning objectives
-------------------
- Explain why exceptions are used and distinguish them from normal control flow.
- Use `try/except/else/finally` blocks correctly.
- Raise and define custom exceptions.
- Handle file I/O errors and convert exceptions to meaningful program responses.

Prerequisites
-------------
- Basic Python (functions, lists, file I/O)
- Python 3.8+

Estimated time
--------------
60–90 minutes

Contents
--------
- Exercise 1: `starters/ex1.py` — Safe division and handling ZeroDivisionError.
- Exercise 2: `starters/ex2.py` — Read integers from a file; handle I/O and value errors.
- Exercise 3: `starters/ex3.py` — Custom exception and input validation.
- Tests: `tests/test_exercises.py` — simple pytest cases.
- Solutions: `solutions/` — reference implementations.
- Rubric: `rubric.md` — grading criteria.

How to run
----------
1. Create a Python virtual environment (optional).
2. Install pytest: `pip install pytest`.
3. Run tests: `pytest -q tests/test_exercises.py`

Hints
-----
- Use specific exceptions (e.g., `ZeroDivisionError`, `FileNotFoundError`) rather than a bare `except`.
- Keep functions small and testable.
- Write meaningful error messages when raising custom exceptions.
