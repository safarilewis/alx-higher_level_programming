#!/usr/bin/python3
"""An empty class"""


class BaseGeometry():
    """A class containing an unimplimented funct"""
    def area(self):

        """Raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates functions"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
