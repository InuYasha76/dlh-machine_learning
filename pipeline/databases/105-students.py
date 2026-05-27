#!/usr/bin/env python3
"""This module is about pymongo."""


def top_students(mongo_collection):
    """
    Function returning students sorted by average score.
    Args:
        mongo_collection (pymongo.collection.Collection).
    Returns:
        collection of students sorted by score desc.
        }
        ]
    """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$name",
            "averageScore": {"$avg": "$topics.score"}
            }
         },
        {"$sort": {"averageScore": -1}},
    ]
    return mongo_collection.aggregate(pipeline)
