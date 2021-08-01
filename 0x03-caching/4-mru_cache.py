#!/usr/bin/python3
""" MRU Caching """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Create a class MRUCache that inherits
    from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()
        self.head, self.tail = 'head', 'tail'
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """ handle elements """
        self.next[head], self.prev[tail] = tail, head

    def element_remove(self, key):
        """ remove element """
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def element_add(self, key, item):
        """ add element """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.prev[self.tail]))
            self.element_remove(self.prev[self.tail])
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)

    def put(self, key, item):
        """ dictionary """
        if key and item:
            if key in self.cache_data:
                self.element_remove(key)
            self.element_add(key, item)

    def get(self, key):
        """ Return the self value """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self.element_remove(key)
            self.element_add(key, value)
            return value
