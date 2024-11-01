#!/usr/bin/env python3
""" MRUCache module """

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache that inherits from BaseCaching, using MRU """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add item to cache, discard MRU item if full """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discarded = next(reversed(self.cache_data))
            print(f"DISCARD: {discarded}")
            self.cache_data.pop(discarded)
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item by key """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key, None)
