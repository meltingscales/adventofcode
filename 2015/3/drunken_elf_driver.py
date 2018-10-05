def get_vector(char):
    if char is '>':  # right
        return (1, 0,)
    elif char is '<':  # left
        return (-1, 0,)
    elif char is '^':  # up
        return (0, 1)
    elif char is 'v':  # down
        return (0, -1)


class Elf:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.history = {}

    def houses_visited(self):
        return len(self.history.keys())

    def location(self):
        return (self.x, self.y,)

    def __add__(self, other):
        self.x += other[0]
        self.y += other[1]

    def go(self, char):
        self + get_vector(char)
        self.visit()

    def visit(self):
        loc = self.location()

        if loc not in self.history:
            self.history[loc] = 0

        self.history[loc] += 1


with open('input') as f:
    data = f.read()

elf = Elf()
elf.visit()  # Visit 0,0

for char in data:
    elf.go(char)

with open('input') as f:
    data = f.read()

print(f"{elf.houses_visited()} houses visited by the elf.")

IS_ROBO = False

santa = Elf()
robosanta = Elf()

for char in data:

    if IS_ROBO:
        robosanta.go(char)
    else:
        santa.go(char)

    IS_ROBO = not IS_ROBO

print(f"{robosanta.houses_visited()} houses visited by Robo-Santa")
print(f"{santa.houses_visited()} houses visited by Santa")

unique_houses = {}
for key, value in santa.history:
    unique_houses[key] = value

for key, value in robosanta.history:
    unique_houses[key] = value

print(f"Unique houses visited by both Santas: {len(unique_houses.keys())}")  # TODO this is wrong
