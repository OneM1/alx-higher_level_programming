#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Add 2 integers.

    Prototype: def add_integer(a, b=98):
    a and b must be integers or floats, otherwise raise a
    TypeError exception with the message a must be an integer
    or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    You are not allowed to import any module
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
