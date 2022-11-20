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

    @width.setter
    def width(self,value):
        """Width setter"""
        self.__width=value

    @height.setter
    def height(self,value):
        """Height Setter"""
        self.__height= value

    @x.setter
    def x(self,value):
        """x Setter"""
        self.__x=value

    @y.setter
    def y(self,value):
        """y Setter"""
        self.__y=value

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @property
    def y(self):
        """Getter for y"""
        return self.__y