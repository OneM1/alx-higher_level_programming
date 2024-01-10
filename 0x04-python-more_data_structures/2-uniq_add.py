#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = set()
    return sum(map(lambda x: unique_int.add(x) or x if x not in unique_int else 0, my_list))
