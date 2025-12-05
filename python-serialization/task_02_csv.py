#!/usr/bin/python3
"""
CSV to JSON Conversion Module
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file into a JSON file named 'data.json'.

    Args:
        csv_filename (str): Path to the input CSV file.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        data_list = []

        with open(csv_filename, newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except Exception:
        return False
