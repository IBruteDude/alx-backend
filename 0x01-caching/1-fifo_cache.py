#!/usr/bin/env python3
"""Module for defining a fifo caching system
"""
from base_cache import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """ FIFO bounded caching system
    """
    def __init__(self):
        """ Initialise a private queue
        """
        super().__init__()
        self.__fifo = deque()

    def put(self, key, item):
        """ Add item in cache with a key, removing first added items if full
        """
        if not key or not item:
            return None
        if not self.cache_data.get(key):
            if len(self.cache_data) == self.MAX_ITEMS:
                old_key = self.__fifo.popleft()
                del self.cache_data[old_key]
                print("DISCARD:", old_key)
        self.__fifo.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item from cache with specified key
        """
        if not key:
            return None
        return self.cache_data.get(key, None)


if __name__ == '__main__':
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
