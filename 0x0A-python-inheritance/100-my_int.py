#!/usr/bin/python3
"""my int"""


class MyInt(int):
    """my is MyInt class"""
    def __eq__(self, other):
        """equal sign"""
        return super().__ne__(other)

    def __ne__(self, other):
        """negation sign"""
        return super().__eq__(other)
