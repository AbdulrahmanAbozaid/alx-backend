#!/usr/bin/env python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache that inherits from BaseCaching, using LIFO """

    def put(self, key, item):
        """ Add item to cache, discard the last item if full """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded = next(reversed(self.cache_data))
            print(f"DISCARD: {discarded}")
            del self.cache_data[discarded]
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item by key """
        return self.cache_data.get(key, None)
