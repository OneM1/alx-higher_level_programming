#!/usr/bin/python3
"""convert a JSON string to a Python data structure."""


def from_json_string(my_str):
    """Convert a JSON string to a Python data structure.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    import json
    return json.loads(my_str)
