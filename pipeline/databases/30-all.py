#!/usr/bin/env python3
"""
Module to list all documents in a MongoDB collection using pymongo
"""


def list_all(mongo_collection):
    """
    Lists all documents in the provided pymongo collection object.
    Returns an empty list if no documents are found.
    """
    return list(mongo_collection.find())
