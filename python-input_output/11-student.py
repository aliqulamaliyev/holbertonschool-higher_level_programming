#!/usr/bin/python3
"""
Student class module with serialization and deserialization
"""


class Student:
    """Defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only include attributes in that list.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        if isinstance(attrs, list):
            filtered_dict = {}
            for key in attrs:
                if key in obj_dict:
                    filtered_dict[key] = obj_dict[key]
            return filtered_dict
        return obj_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance from a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
