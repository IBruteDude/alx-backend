#!/usr/bin/env python3
"""Module for defining a basic caching system
"""
from base_caching import BaseCaching


def put(self, key, item):
    """ Add new item in cache with a key
    """
    if not key or not item:
        return None
    self.cache_data[key] = item


def get(self, key):
    """ Retrieve item from cache with specified key
    """
    if not key:
        return None
    return self.cache_data.get(key, None)


BasicCache = type('BasicCache', (BaseCaching,), {
    '__doc__': 'Basic unbounded caching system',
    'put': put,
    'get': get
})


if __name__ == '__main__':
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))

    if issubclass(BasicCache, BaseCaching):
        print("OK")
    else:
        print("BasicCache doesn't inherit from BaseCaching")
