class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, m, w):
        return self._length * self._width * m * w


a = Road(20, 5000)
print(a.mass(25, 5))
