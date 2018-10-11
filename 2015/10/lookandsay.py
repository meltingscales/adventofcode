import os
import re
import time
import unittest
from functools import lru_cache

from joblib import Memory

memory = Memory(cachedir=
                os.path.join(os.path.dirname(__file__), '__pycache__'),
                verbose=0)

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


@memory.cache
def tokenize_str(s: str = '111133232166565', verbose=False) -> tuple:
    """
    :param s: A look-and-say string.
    :return: The same string, but tokenized into a tuple.
    """

    bucket = []

    while s != '':

        r = re.match(REXP_SAME_DIGIT, s, )

        first = s.replace(r.group(2), '')
        rest = r.group(2)

        if verbose:
            print(f"want to tokenize '{s}'.")

            print(first)
            print(rest)

        bucket.append(first)

        s = rest

    return tuple(bucket)


@memory.cache
def lookandsay(l: tuple) -> str:
    """
    Example:

        f(['11', '777']) -> '2137'

        "Two ones, three sevens."
    """

    if l == tuple():
        return ''

    ret = ""

    for s in l:

        if s != '':
            ret += lasonce(s)

    return ret


class TestLASOnce(unittest.TestCase):

    def testBasic(self):
        self.assertEqual(lasonce('11111'), '51')

        self.assertEqual(lasonce('33'), '23')


class TestTokenizer(unittest.TestCase):

    def testBasic(self):
        self.assertEqual(tokenize_str(''), [])

        self.assertEqual(tokenize_str('0010'), ('00', '1', '0'))

        self.assertEqual(tokenize_str('112211'), ('11', '22', '11'))


class TestAll(unittest.TestCase):

    def testAllOfEm(self):
        self.assertEqual(lookandsay(tokenize_str('1111')), '41')

        self.assertEqual(lookandsay(tokenize_str('13')), '1113')

        self.assertEqual(lookandsay(tokenize_str('1113')), '3113')


if __name__ == '__main__':

    with open('input', 'r') as f:
        word = f.readline().strip()

    t = time.time()

    for i in range(0, 51):
        print(f"{time.time() - t} sec\n"
              f"{i:3d}: len = {len(word)};\n"
              f"{word[0:100]}\n"
              f"->\n"
              f"{lookandsay(tokenize_str(word))[0:100]}\n")

        word = lookandsay(tokenize_str(word))
