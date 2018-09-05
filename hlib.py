class Location:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):

        # Adding two locations
        if isinstance(other, Location):
            self.x += other.x
            self.y += other.y

        # Adding a number to this location
        if isinstance(other, float) or \
                isinstance(other, int):
            self.x += other
            self.y += other
