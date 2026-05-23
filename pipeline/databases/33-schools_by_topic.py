#!/usr/bin/env python3
"""
Module providing a function to search schools by topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic 

    Args:
        mongo_collection: The PyMongo collection.
        topic (str): The topic to look up within the schools.

    Returns:
        list: A list of schools proposing the topic.
    """
    return list(mongo_collection.find({ "topics": topic }))
