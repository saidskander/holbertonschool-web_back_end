#!/usr/bin/env python3
""" specific topic """


def schools_by_topic(mongo_collection, topic):
    """ specific topic """
    return mongo_collection.find({ "topics": topic })
