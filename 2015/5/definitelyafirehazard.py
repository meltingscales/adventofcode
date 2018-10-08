import re
from copy import deepcopy
import unittest
from random import randint

COMMAND_REXP = r'(.+?)(\d*,\d*) through (\d*,\d*)'
CTYPES = [
    'turn on',
    'turn off',
    'toggle',
]


class Command(object):
    def __init__(self, command: str, start: tuple, end: tuple):
        self.command = command
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.command} {self.start}-{self.end}"


def parse_command(cstr: str) -> Command:
    result = re.search(COMMAND_REXP, cstr)

    com, p1s, p2s = result.groups()

    com = com.strip()

    p1 = tuple([int(s) for s in p1s.split(',')])
    p2 = tuple([int(s) for s in p2s.split(',')])

    return Command(com, p1, p2)


def rangealways(start=0, stop=10, step=1):
    """
    Range that always yields values.
    """
    # i.e. range(7, 3, 1)...
    if (start > stop) and step > 0:  # then we wouldn't iterate
        for i in range(start, stop - 1, -step):
            yield i

    # i.e. range(3, 7, -1)...
    elif (start < stop) and step < 0:  # again, we wouldn't iterate
        for i in range(start, stop + 1, -step):
            yield i

    else:
        for i in range(start, stop + 1, step):
            yield i


class Light(object):
    state = False

    def toggle(self):
        self.state = not self.state

    def on(self):
        self.state = True

    def off(self):
        self.state = False

    def __str__(self):
        if self.state:
            return "#"
        return "."


class LightGrid(object):

    def apply_command(self, c: Command):
        if 'turn on' in c.command:
            self.on(c.start, c.end)

        elif 'turn off' in c.command:
            self.off(c.start, c.end)

        elif 'toggle' in c.command:
            self.toggle(c.start, c.end)

    def _generate_grid(self):
        self.grid = [deepcopy([Light() for _ in range(0, self.width)])
                     for _ in range(0, self.height)]

    def __init__(self, *args, **kwargs):
        self.height = kwargs.pop('height', 5)
        self.width = kwargs.pop('width', 3)

        self._generate_grid()

    def __getitem__(self, pos) -> Light:
        x, y = pos
        # print(f"Want item at '{pos}'!")
        return self.grid[y][x]

    def __setitem__(self, key: tuple, value: Light):
        x, y = key
        self.grid[y][x] = value

    def _apply(self, start: tuple, end: tuple, func=lambda x: ()) -> None:
        p1x, p1y = start
        p2x, p2y = end

        for i in rangealways(p1x, p2x):
            for j in rangealways(p1y, p2y):
                func(self[i, j])

    def on(self, start: tuple, end: tuple):
        self._apply(start, end, lambda l: l.on())

    def off(self, start: tuple, end: tuple):
        self._apply(start, end, lambda l: l.off())

    def toggle(self, start: tuple, end: tuple):
        self._apply(start, end, lambda l: l.toggle())

    def render(self, sep='\n'):
        for row in self.grid:
            for l in row:
                print(l, end='')
            print(sep, end='')

    def render_lights_statusrep(self):
        return f"{self.lights_on():10d} on, " \
               f"{self.lights_off():10d} off."

    def lights_matching(self, value=True):

        total = 0

        for i in range(0, self.width):

            for j in range(0, self.height):

                if self[i, j].state == value:
                    total += 1

        return total

    def lights_off(self):
        return self.lights_matching(False)

    def lights_on(self):
        return self.lights_matching(True)

    def lights_total(self):
        return self.width * self.height


class TestLightGrid(unittest.TestCase):
    def lightGridSanityCheck(self, lg: LightGrid):
        lg = deepcopy(lg)

        # Make sure all ON+OFF = ALL LIGHTS
        self.assertEqual(lg.lights_total(), lg.lights_on() + lg.lights_off())

        # Turn them all on
        lg.on((0, 0), (lg.width - 1, lg.height - 1))

        # Make sure all lights are on.
        self.assertEqual(lg.lights_on(), lg.lights_total())
        self.assertEqual(lg.lights_on(), lg.width * lg.height)

        # Turn them all off
        lg.off((0, 0), (lg.width - 1, lg.height - 1))

        # Make sure all lights are off.
        self.assertEqual(lg.lights_off(), lg.lights_total())
        self.assertEqual(lg.lights_off(), lg.width * lg.height)

        # Turn one column on.
        lg.on((0, 0), (0, lg.height - 1))

        # Make sure that one column is on.
        self.assertEqual(lg.lights_on(), lg.height)

    def test_simple(self):
        lg = LightGrid(width=randint(10, 20), height=randint(10, 20))

        self.lightGridSanityCheck(lg)


class TestParseCommand(unittest.TestCase):
    def test_parse_command(self):
        random_command = CTYPES[randint(0, len(CTYPES) - 1)]

        p1x = randint(0, 999)
        p1y = randint(0, 999)

        p2x = randint(0, 999)
        p2y = randint(0, 999)

        command = f"{random_command} {p1x},{p1y} through {p2x},{p2y}"

        c = parse_command(command)

        self.assertEqual(c.start, (p1x, p1y))
        self.assertEqual(c.end, (p2x, p2y))
        self.assertEqual(c.command, random_command)


if __name__ == '__main__':
    # unittest.main()

    lg = LightGrid(height=1000, width=1000)

    with open('input', 'r') as f:
        for line in f.readlines():
            lg.apply_command(parse_command(line))

            print(lg.render_lights_statusrep())

    print("Final answer:")
    print(lg.render_lights_statusrep())
