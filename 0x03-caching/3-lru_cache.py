#!/usr/bin/python3
""" LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Create a class LRUCache that inherits
        from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()
        self.head, self.tail = '-', '='
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
        """ add an element """
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.next[self.head]))
            self.element_remove(self.next[self.head])

    def put(self, key, item):
        """ dictionary """
        if key and item:
            if key in self.cache_data:
                self.element_remove(key)
            self.element_add(key, item)

    def get(self, key):
        """ Return the self value"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self.element_remove(key)
            self.element_add(key, value)
            return value
