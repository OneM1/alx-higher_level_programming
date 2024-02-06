#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads the content of a text file .

    Args:
        filename : The name of the file to read. Default is an empty string.

    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
