#!/usr/bin/python3
"""
Contains a certain inherits_from function
"""


def inherits_from(obj, a_class):
    """Returns True only if obj is sub-class of a_class, otherwise False"""
    return (type(obj) != a_class and issubclass(type(obj), a_class))
