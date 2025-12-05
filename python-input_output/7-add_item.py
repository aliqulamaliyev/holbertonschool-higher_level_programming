#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list,
then saves them to a file as a JSON representation.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing items or create empty list if file doesn't exist
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add all command-line arguments (excluding the script name)
items.extend(sys.argv[1:])

# Save updated list back to the file
save_to_json_file(items, filename)
