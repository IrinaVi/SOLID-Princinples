# Created by Barbara Liskov in a 1987, this states that objects should be replaceable
# by their subtypes without altering how the program works.
# In other words, derived classes must be substitutable for their base classes without causing errors.

class Rectangle():
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def area(self):
        return self.get_width() * self.get_height()

class Square(Rectangle):
    def __init__(self, width):
        self._width = width
        self._height = width

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
        self._height = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height
        self._width = height