#!/usr/bin/python3
"""Base Class"""


class Base:
    """Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
    if (id is not None):
        self.id = id
    else:
        __nb_objects = __nb_objects + 1
