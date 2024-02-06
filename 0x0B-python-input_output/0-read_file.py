#!/usr/bin/python3
"""Module to read a text file and print its contents to stdout."""


def read_file(filename=""):
    """Read the contents of a text file and print to stdout.

    Args:
        filename (str): The name of the text file to read.

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')


if __name__ == "__main__":
    read_file()
