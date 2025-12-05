#!/usr/bin/python3
"""
Function that returns the dictionary description with simple data structure
for JSON serialization of an object.
"""


def class_to_json(obj):
    """Returns the dictionary representation of  object for JSON serialization.

    Args:
        obj: Instance of a class.

    Returns:
        dict: Dictionary of the instance attributes.
    """
    return obj.__dict__.copy()
