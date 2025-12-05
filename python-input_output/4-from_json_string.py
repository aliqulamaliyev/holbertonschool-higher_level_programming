#!/usr/bin/python3
"""
Function that returns the Python object represented by a JSON string
"""

import json


def from_json_string(my_str):
    """Converts a JSON string to a Python object.

    Args:
        my_str (str): JSON string representation.

    Returns:
        object: Python object represented by the JSON string.
    """
    return json.loads(my_str)
