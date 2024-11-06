#!/usr/bin/env python3
""" FIFOCache module """

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ FIFOCache that inherits from BaseCaching, using FIFO """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add item to cache, discard the first item if full """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded = next(iter(self.cache_data))
            print(f"DISCARD: {discarded}")
            self.cache_data.pop(discarded)
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item by key """
        return self.cache_data.get(key, None)
