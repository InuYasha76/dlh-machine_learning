#!/usr/bin/env python3
"""
Module updating school documents in MongoDB.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' array field for all schools matching the given name.
    Args:
        mongo_collection (pymongo.collection): The PyMongo collection.
        name (str): The name of the school to update.
        topics (list of str): The blist of topics to set for the school.
    Returns:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
