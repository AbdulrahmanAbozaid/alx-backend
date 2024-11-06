#!/usr/bin/env python3
"""
Cashing at once
"""
BaseCaching = __import__("base_caching").BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """Basix"""

    def __init__(self):
        """Init"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        if not key or not item:
            return
        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
            f_key = self.cache_data.popitem()
            print(f"DISCARD: {f_key[0]}")
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key, default=None)
