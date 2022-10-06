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
    """Sets the size of the square"""
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the square

         Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

