import re


def nice(s: str, verbose: bool = False):
    """Returns whether or not a string, `s`, is 'nice'."""
    patterns = [
        r'[aeiou].*[aeiou].*[aeiou]',  # three vowels
        r'([a-zA-Z])\1',  # one letter that appears twice in a row
    ]

    forbidden = [  # These cannot appear in a nice string.
        'ab',
        'cd',
        'pq',
        'xy',
    ]

    for pat in patterns:  # For all patterns,
        if len(re.findall(pat, s)) is 0:  # If it fails EVEN ONE, return False.

            if verbose:
                print(f"'{s}' is naughty because it fails to match '{pat}'.")

            return False

    for f in forbidden:  # For all forbidden sequences,
        if f in s:  # If it matches JUST ONE, return False.

            if verbose: print(f"'{s}' is naughty because it contains '{f}'.")

            return False

    if verbose: print(f"'{s}' is nice!")

    return True


def nices(filepath='input', verbose: bool = False) -> int:
    n = 0

    if verbose: print(f"How nice is '{filepath}'?")

    with open(filepath, 'r') as f:
        for line in f.readlines():
            if nice(line.strip(), verbose):
                n += 1

    return n


# print(f"{nices('input2', verbose=True)}")

print(f"{nices('input', verbose=True)}")
