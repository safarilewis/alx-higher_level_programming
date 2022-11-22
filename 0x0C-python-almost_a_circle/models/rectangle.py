#!/usr/bin/python3
"""
Rectangle that inherits from base class
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from base"""
    def __init__(self, width,height,x=0,y=0,id=None):
        """Initializes a new rectangle"""
        self.width = width
        self.height=height
        self.x=x
        self.y=y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width. setter
    def width(self,value):
        """Width setter/getter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    
    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self,value):
        """Height Setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height= value
    
    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self,value):
        """x Setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y Setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
