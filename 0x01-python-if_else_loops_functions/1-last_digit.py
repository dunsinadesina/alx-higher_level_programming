#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number > 10 else number % -10
print(f"Last digit of {number} is {last_digit} and is ", end="")
if (0 < last_digit < 6):
    print(f"less than 6 and not 0")
elif (last_digit > 5):
    print(f"greater than 5")
elif (last_digit == 0):
    print(f"0")
