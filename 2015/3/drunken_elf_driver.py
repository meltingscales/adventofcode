from ...hlib import *


class Elf:
    history = {}

    def __init__(self, location=Location(0, 0)):
        self.location = location


with open('input') as f:
    data = f.read()
