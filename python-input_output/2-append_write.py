#!/usr/bin/python3
def append_write(filename="", text=""):
    """Appends a string at the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file.
        text (str): The text to append.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
