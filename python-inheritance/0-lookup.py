#!/usr/bin/python3
""" Return the attributes of an object"""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return [attr for attr in dir(obj) if not
            callable(getattr(obj, attr)) or callable(getattr(obj, attr))]
