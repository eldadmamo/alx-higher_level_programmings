#!/usr/bin/python3
"""object to a Save"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save an object JSON file.

    Args:
        my_obj (any): The object to be save JSON file.
        filename (str): The name of the file to the object 

    Returns:
        None

    Example:
        # Saving a dictionary JSON file
        data = {"name": "John", "age": 30}
        save_to_json_file(data, "output.json")
        # The contents of data to output.json in JSON format

        # Saving a list to a JSON file
        data = [1, 2, 3, 4, 5]
        save_to_json_file(data, "output.json")
        # The contents of data  to output.json in JSON format
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
