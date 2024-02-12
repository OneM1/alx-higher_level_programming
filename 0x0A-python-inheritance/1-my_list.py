#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A class that inherits from list and adds functionality to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        print(sorted(self))
