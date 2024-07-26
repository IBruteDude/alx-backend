#!/usr/bin/env python3
"""Module for defining a basic caching system
"""
from heapq import heappop, heappush
from base_caching import BaseCaching


def __init__(self):
    """ Initialise a private heap
    """
    super(self.__class__, self).__init__()
    self.__mru = []
    self.__age = 0


def put(self, key, item):
    """ Add item in cache with a key, removing least recently used if full
    """
    if not key or not item:
        return None
    if not self.cache_data.get(key):
        if len(self.cache_data) == self.MAX_ITEMS:
            old_key = heappop(self.__mru)
            del self.cache_data[old_key[1]]
            print("DISCARD:", old_key[1])
    else:
        for i, k in enumerate(self.__mru):
            if k[1] == key:
                self.__mru.pop(i)

    heappush(self.__mru, (self.__age, key))
    self.cache_data[key] = item
    self.__age -= 1


def get(self, key):
    """ Retrieve item from cache with specified key
    """
    if not key:
        return None
    value = self.cache_data.get(key, None)
    self.put(key, value)
    return value


MRUCache = type('MRUCache', (BaseCaching,), {
    '__doc__': 'MRU bounded caching system',
    '__init__': __init__,
    'put': put,
    'get': get
})


if __name__ == '__main__':
    my_cache = MRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
