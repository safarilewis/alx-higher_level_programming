#!/usr/bin/python3
"""
Represents a square
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square"""
    def __init__(self, x=0, y=0, id=None):
        """initializes the square"""
        super().__init__(size, size, x, y, id)

     @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
