#!/usr/bin/env python3
""" class FIFO Cache inherits from caching system """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache that inhe from a caching system """
    def __init__(self):
        """ init """
        super().__init__()

    def put(self, key, item):
        """  cache append item """
        if (not key or not item):
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            print("DISCARD: {}".format(next(iter(self.cache_data))))
            self.cache_data.pop(next(iter(self.cache_data)))
        self.cache_data[key] = item

    def get(self, key):
        """ from key get the item """
        if (not key or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]
