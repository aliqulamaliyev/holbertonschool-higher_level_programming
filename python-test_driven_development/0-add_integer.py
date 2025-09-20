#!/usr/bin/python3
"""
This module defines the function add_integer.
It adds two integers or floats (after casting them to integers).
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Parameters:
        a (int or float): First number.
        b (int or float): Second number, defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

