#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
Last_digit = number_str[-1:]
text = "Last digit of"
text2 = "and is less than 6 and not 0"
if int(Last_digit) > 5:
    print("{} {} is {} and is great than 5".format(text, number, Last_digit))
elif int(Last_digit) == 0:
    print("{} {} is {} and is 0".format(text, number, Last_digit))
elif int(Last_digit) < 6 and Last_digit != '0':
    print("{} {} is {} {}".format(text, number, Last_digit, text2))
else:
    print("Wrong Type")
