#!/usr/bin/python3
"""
Function that appends a string at the end of a text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF-8 text file.

    Args:
        filename (str): Name of the file.
        text (str): Text to write.

    Returns:
        int: Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
