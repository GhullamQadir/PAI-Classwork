"""Solution for exercise 2: read_ints."""

def read_ints(filename):
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
                    # skip invalid lines
                    continue
    except FileNotFoundError:
        return []
    return ints
