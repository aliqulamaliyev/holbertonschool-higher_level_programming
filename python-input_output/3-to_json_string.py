#!/usr/bin/python3
"""
Function that returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of a Python object.

    Args:
        my_obj: Any Python object that can be serialized.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
