#!/usr/bin/python3
"""Now lets deal with Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ I hate documentation"""
    def __init__(self, size):

        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
