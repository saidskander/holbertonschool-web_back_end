#!/usr/bin/env python3
""" Change topics """


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document by names """
    return mongo_collection.update_many({ "name": name }, { "$set": { "topics": topics } })
