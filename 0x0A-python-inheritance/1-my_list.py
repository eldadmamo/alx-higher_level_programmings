#!/usr/bin/python3
"""check for list"""


class MyList(list):
    """inherit list"""
    def print_sorted(self):
        print(sorted(self))
