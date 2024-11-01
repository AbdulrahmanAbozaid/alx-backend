#!/usr/bin/env python3
""" LFU Cache Module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching and implements an LFU cache """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.frequency = {}  # Stores frequency of each key
        self.usage_order = {}  # Stores order of keys with same frequency

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        # Update existing key
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1  # Increment frequency
            self.usage_order[key] = self.frequency[key]  # Update usage order
        else:
            # If cache exceeds MAX_ITEMS, we need to discard an item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key(s)
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, freq in self.frequency.items() if freq == min_freq]

                # If there's a tie, remove the least recently used (oldest)
                if len(lfu_keys) > 1:
                    oldest_key = min(lfu_keys, key=lambda k: self.usage_order[k])
                else:
                    oldest_key = lfu_keys[0]

                # Remove the oldest key
                print("DISCARD:", oldest_key)
                del self.cache_data[oldest_key]
                del self.frequency[oldest_key]
                del self.usage_order[oldest_key]

            # Add the new key-value pair
            self.cache_data[key] = item
            self.frequency[key] = 1  # Set initial frequency to 1
            self.usage_order[key] = 0  # Set initial order to 0 for new keys

    def get(self, key):
        """ Retrieve an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency and usage order for the accessed key
        self.frequency[key] += 1
        self.usage_order[key] = self.frequency[key]  # Update usage order to current frequency
        return self.cache_data[key]
