from random import randrange


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def distance_to(self, point):
        return abs(point.x - self.x) + abs(point.y - self.y)

    def set(self, point):
        self.x = point.x
        self.y = point.y

    def __eq__(self, point):
        return point.x == self.x and point.y == self.y

    def __ne__(self, point):
        return not (self == point)

    def randomize(self, x_border, y_border):
        self.x = randrange(0, x_border)
        self.y = randrange(0, y_border)

    def __copy__(self):
        return type(self)(self.x, self.y)

    def copy(self):
        return type(self)(self.x, self.y)

    def x_distance(self, point):
        return abs(self.x - point.x)

    def y_distance(self, point):
        return abs(self.y - point.y)

    def greater_distance_is_in_x(self, point):
        return self.x_distance(point) > self.y_distance(point)

    def greater_distance_is_in_y(self, point):
        return self.y_distance(point) > self.x_distance(point)
