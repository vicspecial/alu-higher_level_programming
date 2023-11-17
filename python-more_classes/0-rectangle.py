#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)


When you run this code, it should output:


<class '0-rectangle.Rectangle'>
{}


