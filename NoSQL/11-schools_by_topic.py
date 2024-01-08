#!/usr/bin/env python3
""" function that returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ Return the list with the good topics """
    topic_list = []
    try:
        for _ in mongo_collection.find(
            {"topics": topic}
        ):
            topic_list.append(_)
        return topic_list
    except:
        pass
