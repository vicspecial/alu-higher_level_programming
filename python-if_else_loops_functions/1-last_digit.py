#!/usr/bin/python3
import random
import random

# Generate a random signed number between -10000 and 10000
number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = ads(number) % 10

if number > 0 < last_digit > 5:
    print(f"Last digit of {number} is {last_digit}\
  and is greaterthan 5")
elif last_digit == 0:
    print(f"last digit of {number} is {last_digit}\
  and is 0")
elif number < 0 < last_digit:
    print(f"Last digit of {number} is -{last_digit}\
  and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_digit}\
  and is less than 6 and not 0")          
