#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
last_number = number % 10
if (number < 0):
    number *= -1
    last_number = number % 10
    last_number *= -1
    number *= -1

if (last_number > 5):
    print(f"{str} {number:d} is {last_number:d} and is greater than 5")

elif (last_number == 0):
    print(f"{str} {number:d} is {last_number:d} and is 0")
elif (last_number < 6 and last_number != 0):
    print(f"{str} {number:d} is {last_number:d} and is less than 6 and not 0")
