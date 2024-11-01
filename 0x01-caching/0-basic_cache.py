#!/usr/bin/env python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache that inherits from BaseCaching with no limit """

    def put(self, key, item):
        """ Add item to cache without limit """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item by key """
        return self.cache_data.get(key, None)
