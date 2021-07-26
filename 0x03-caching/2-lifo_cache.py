#!/usr/bin/python3
""" class LIFO Cache """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ class LIFOCache """
    def __init__(self):
        """ init """
        super().__init__()

    def put(self, key, item):
        """ append an item """
        if (not key or not item):
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            removed = self.cache_data.popitem()
            print("DISCARD: {}".format(removed[0]))
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item """
        if (not key or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]
