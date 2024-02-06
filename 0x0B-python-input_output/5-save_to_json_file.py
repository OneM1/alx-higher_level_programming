#!/usr/bin/python3
"""save an object to a text file using JSON representation."""


def save_to_json_file(my_obj, filename):
    """Save an object to a text file using JSON representation.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file to save the object to.

    Returns:
        None
    """
    import json
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
