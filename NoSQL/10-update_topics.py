#!/usr/bin/env python3
""" function that changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """ upadte doc with specific name """
    try:
        result = mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
        )
    except:
        pass
