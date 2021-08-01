#!/usr/bin/python3
""" class LFUCache that inherit
    from BaseCaching and caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ class LFUCache inherit BaseCaching """
    QUEUE = []
    usage = {}

    def __init__(self):
        """ initiliaze """
        super().__init__()

    def _update(self, KeyToRemove, KeyToAppend):
        """ update queue
        """
        self.__class__.QUEUE.remove(KeyToRemove)
        self.__class__.QUEUE.append(KeyToAppend)

    def put(self, key, item):
        """ add item """
        if (not key or not item):
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                if key in self.__class__.QUEUE:
                    self.__class__.QUEUE.remove(key)
                if key in self.__class__.usage:
                    usageFrequency = self.__class__.usage[key]
                    self.__class__.usage.pop(key, None)
                    self.__class__.usage[key] = usageFrequency + 1
                else:
                    self.__class__.usage[key] = 2

            else:
                if len(self.__class__.QUEUE) != 0:
                    print("DISCARD: {}".format(
                        self.__class__.QUEUE[0]))
                    keyToDelete = self.__class__.QUEUE[0]
                    del self.cache_data[keyToDelete]
                    self.cache_data[key] = item
                    self._update(keyToDelete, key)
                else:
                    keyx = sorted(self.__class__.usage,
                                  key=self.__class__.usage.get)[0]
                    print("DISCARD: {}".format(keyx))
                    del self.cache_data[keyx]
                    self.__class__.usage.pop(keyx, None)
                    self.cache_data[key] = item
                    self.__class__.QUEUE.append(key)

        else:

            self.cache_data[key] = item
            self.__class__.QUEUE.append(key)

    def get(self, key):
        """ slef key get item"""
        if (not key or key not in self.cache_data.keys()):
            return None

        if key not in self.__class__.usage:
            self.__class__.usage[key] = 2
            self.__class__.QUEUE.remove(key)

        else:
            self.__class__.usage[key] = self.__class__.usage[key] + 1

        return self.cache_data[key]
