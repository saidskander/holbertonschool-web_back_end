#!/usr/bin/env python3
""" list all documents in python """
import pymongo


def list_all(mongo_collection):
    """ lists documents in a collection """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
