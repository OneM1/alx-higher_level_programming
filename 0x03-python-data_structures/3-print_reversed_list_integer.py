#!/usr/bin/python3
def print_reversed_list_integer(my_list=None):
    if my_list is None:
        my_list=[]
    reverse=my_list[::-1]
    for i in reverse:
        print("{}".format(i))
