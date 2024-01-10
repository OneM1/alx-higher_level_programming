#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
Last_digit = number_str[-1:]
if int(Last_digit) > 5:
    print("Last digit of {} is {} and is great than 5".format(number, Last_digit))
elif int(Last_digit) == 0:
    print("Last digit of {}  is {} and is 0".format(number, Last_digit))
elif int(Last_digit) < 6 and Last_digit != '0':
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, Last_digit))
else:
    print("Wrong Type")
