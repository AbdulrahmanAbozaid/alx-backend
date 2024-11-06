#!/usr/bin/env python3
""" LIFOCache module """
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache that inherits from BaseCaching, using LIFO """

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add item to cache, discard the last item if full """
        if key is None or item is None:
            return
        if key not in self.cache_data and\
                len(self.cache_data) >= self.MAX_ITEMS:
            discarded = self.cache_data.popitem()
            print(f"DISCARD: {discarded[0]}")
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item by key """
        return self.cache_data.get(key, None)
