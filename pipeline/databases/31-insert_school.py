#!/usr/bin/env python3
"""
Module to insert a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document into the provided mongo_collection.
    Returns the new_id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
