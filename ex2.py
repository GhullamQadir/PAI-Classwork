"""Exercise 2: Read integers from a file.

Implement `read_ints(filename)` that reads lines from a text file and returns a
list of integers. Handle missing files and lines that cannot be converted to int.
For a missing file, return an empty list. For lines that are invalid, skip them.
"""

def read_ints(filename):
    """Read integers from `filename` and return as a list.

    On FileNotFoundError return an empty list. Skip lines that cannot be parsed.
    """
    ints = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    ints.append(int(line))
                except ValueError:
                    continue
    except FileNotFoundError:
        return []
    return ints
