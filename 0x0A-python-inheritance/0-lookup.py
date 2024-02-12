#!/usr/bin/python3

"""
Module provides a function to retrieve the list of
available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list object containing the names of attributes
    and methods of the input object.

    Args:
        obj: An object whose attributes and methods are to be looked up.

    Returns:
        A list containing the names of attributes and methods of the
        input object.
    """
    return dir(obj)
