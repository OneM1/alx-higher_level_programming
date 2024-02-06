#!/usr/bin/python3
"""convert an object to its JSON representation."""


def to_json_string(my_obj):
    """Convert an object to its JSON representation.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    import json
    return json.dumps(my_obj)
