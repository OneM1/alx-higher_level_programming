#!/usr/bin/python3
"""Module to append a string at end  return number of characters added.
"""


def append_write(filename="", text=""):
    """Append a string at the end of return number of characters added.

    Args:
        filename (str): The name of the text file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    print(append_write())

