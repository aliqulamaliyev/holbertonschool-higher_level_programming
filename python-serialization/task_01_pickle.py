#!/usr/bin/python3
"""
Pickle Serialization Module

This module defines a CustomObject class that can be serialized
and deserialized using the pickle module.
"""

import pickle


class CustomObject:
    """A class representing a custom object with serialization support."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject instance.

        Args:
            name (str): Name of the object.
            age (int): Age of the object.
            is_student (bool): Whether the object represents a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle.

        Args:
            filename (str): File path to save the serialized object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject from a file.

        Args:
            filename (str): File path to load the object from.

        Returns:
            CustomObject or None: The deserialized object or None on error.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            return None
