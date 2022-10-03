#!/usr/bin/python3
"""
Rectangle class that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """represents a rectangle"""

    def __init__(self, width, height, x, y):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ width getter and setter"""
    @property
    def width(self):
        """Getter for the width attribute"""
        return self.__width
        
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """ height getter and setter"""
    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__width
        
    @height.setter
    def height(self, value):
         if type(value) is not int:
            raise TypeError("height must be an integer")
         if value < 0:
            raise ValueError("height must be > 0")
         self.__height = value

    """x getter and setter"""
    @property
    def x(self):
        """Getter for the x attribute"""
        return self.__x
        
    @x.setter
    def x(self, value):
         if type(value) is not int:
            raise TypeError("x must be an integer")
         if value < 0:
            raise ValueError("x must be >= 0")
         self.__x = value

    """ y getter and setter"""
    @property
    def y(self):
        """Getter for the y attribute"""
        return self.__x
        
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    #Area
    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self__height
        
    #Display
    def display(self):
        """Displays a rectangle in terms of #"""

    #Update
    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1