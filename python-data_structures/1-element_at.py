#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]

# Testing the function
print(element_at([1, 2, 3], 1))  # Output: 2
print(element_at([1, 2, 3], 0))  # Output: 1
print(element_at([1, 2, 3], 2))  # Output: 3
print(element_at([1, 2, 3], 3))  # Output: None
print(element_at([1, 2, 3], -1))  # Output: None
print(element_at([1], 0))  # Output: 1
print(element_at([1], 1))  # Output: None
