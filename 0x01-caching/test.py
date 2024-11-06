#!/usr/bin/env python3
"""
Cashing at once
"""
BaseCaching = __import__("base_caching").BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """Basix"""

    def __init__(self):
        """Init"""
        super().__init__()
        self.cache_count = {}
        self.cache_data = OrderedDict()
    
    def __getminitem(self):
        """Get item by its age"""
        min_count = min(self.cache_count.values())
        for k in self.cache_data:
            if self.cache_count[k] == min_count:
                return k

    def put(self, key, item):
        if not key or not item:
            return
        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
            f_key = self.__getminitem()
            del self.cache_data[f_key]
            del self.cache_count[f_key]
            print(f"DISCARD: {f_key}")

        if key in self.cache_data:
            self.cache_count[key] += 1
        else:
            self.cache_count[key] = 1

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        if key in self.cache_data:
            self.cache_count[key] += 1
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key, None)
