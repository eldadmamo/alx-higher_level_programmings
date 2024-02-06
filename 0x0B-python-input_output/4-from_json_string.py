#!/usr/bin/python3
"""JSON object"""

import json


def from_json_string(my_str):
    """
    JSON string into a JSON object.

    Args:
        my_str (str): The converted JSON String.

    Returns:
        dict: The parsed JSON object input string.
    """
    return json.loads(my_str)
