import re
import unittest

REXP_SAME_DIGIT = r'(\d)\1*(.*)'


def lasonce(s: str = '3333') -> str:
    """
    :param s: A repeating string of the same number.
    :return: How many numbers there are of a certain number.
    Example:
        f('33333') -> '53'
    Invalid usage:
        f('33311')
    """
    return str(len(s)) + s[0]


def tokenize_str(s: str = '111133232166565', _bucket=None, verbose=False) -> str:
    """
    :param s: A look-and-say string.
    :return: The same string, but tokenized into a list.
    """

    if _bucket is None:
        _bucket = []

    if s == '':
        return _bucket

    r = re.match(REXP_SAME_DIGIT, s, )

    first = s.replace(r.group(2), '')
    rest = r.group(2)

    if verbose:
        print(f"want to tokenize '{s}'.")

        print(first)
        print(rest)

    _bucket.append(first)

    if rest == '':
        return _bucket
    else:
        return tokenize_str(rest, _bucket)


class TestLASOnce(unittest.TestCase):

    def testBasic(self):
        self.assertEqual(lasonce('11111'), '51')

        self.assertEqual(lasonce('33'), '23')


class TestTokenizer(unittest.TestCase):

    def testBasic(self):
        self.assertEqual(tokenize_str(''), [])

        self.assertEqual(tokenize_str('0'), ['0'])

        self.assertEqual(tokenize_str('0010'), ['00', '1', '0'])

        self.assertEqual(tokenize_str('112211'), ['11', '22', '11'])


if __name__ == '__main__':
    print("hi")
