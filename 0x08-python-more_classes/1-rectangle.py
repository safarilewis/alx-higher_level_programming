#!/usr/bin/python3
"""
Defines a class rectangle
"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0,height=0):
        """Initialized the rectangle"""
        self.height = height
        self.width = width

        @property
