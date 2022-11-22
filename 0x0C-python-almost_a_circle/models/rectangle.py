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
        """Width setter/getter"""
        self.__width = value

    @property
    def width(self):
        return self.__width
    

    @height.setter
    def height(self,value):
        """Height Setter"""
        self.__height= value

    @property
    def height(self):
        """Height getter"""
        return self.__height
    
    @x.setter
    def x(self,value):
        """x Setter"""
        self.__x=value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @y.setter
    def y(self,value):
        """y Setter"""
        self.__y=value

    @property
    def y(self):
        """Y getter"""
        return self.__y
    