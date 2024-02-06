#!/usr/bin/python3
"""Object from a file"""

import json


def load_from_json_file(filename: str) -> dict:
    """
    Load JSON file

    Args:
        filename (str): The name of the JSON file.

    Returns:
        dict: loaded JSON object.

    Raises:
        FileNotFoundError: If specified file does not occur.
        json.JSONDecodeError: file contents are not valid JSON.
    """
    with open(filename, "r") as file:
        return json.load(file)
