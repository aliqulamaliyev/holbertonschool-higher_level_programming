#!/usr/bin/python3
"""
Function that creates a Python object from a JSON file
"""

import json


def load_from_json_file(filename):
    """Loads a Python object from a JSON file.

    Args:
        filename (str): Name of the JSON file.

    Returns:
        object: Python object represented in the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
