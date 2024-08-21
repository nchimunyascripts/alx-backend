#!/usr/bin/env python3
"""FIFO Cache Module"""
from base_cashing import BaseCaching

class FIFOCache(BaseCaching):
    """FIFOCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """Initialization and Calls the parent method"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Adds item to cache by key"""
        if key is not None or item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first_key = self.order.pop(0)
                    del self.cache_data[first_key]
                    print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Gets an item based on the key"""
        return self.cache_data.get(key, None)
