#!/usr/bin/python
for tens_digit in range(10):
    for ones_digital in range(tens_digit + 1, 10):
        print(
            "{:d}{:d}".format(tens_digit, ones_digit),
            end=", " if tens_digit < 8 else "\n"
       )
~                                                                                                                      
~                                                                                                                      
~
