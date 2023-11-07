#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num in my_list:
        if isinstance(num, int):
            print("{:d}".format(num))
        else:
            raise Exception("List contains non-integer values")

# Testing the function
try:
    print_list_integer([1, 2, 3])
except Exception as e:
    print(e)

try:
    print_list_integer([1])
except Exception as e:
    print(e)

try:
    print_list_integer([])
except Exception as e:
    print(e)

try:
    print_list_integer([1, 2, "H", 9])
except Exception as e:
    print(e)
