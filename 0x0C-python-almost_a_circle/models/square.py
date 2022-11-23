#!/usr/bin/python3
"""This contains a square class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """"Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor that initializes the class"""
        super.__init__(size, size, x, y, id)

    
        