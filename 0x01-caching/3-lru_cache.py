#!/usr/bin/env python3
"""Module for defining an lru caching system
"""
from heapq import heappop, heappush


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")


class LRUCache(BaseCaching):
    """ LRU bounded caching system
    """
    def __init__(self):
        """ Initialise a private queue
        """
        super().__init__()
        self.__lru = []
        self.__age = 0

    def put(self, key, item):
        """ Add item in cache with a key, removing least recently usef if full
        """
        if not key or not item:
            return None
        if not self.cache_data.get(key):
            if len(self.cache_data) == self.MAX_ITEMS:
                old_key = heappop(self.__lru)
                del self.cache_data[old_key[1]]
                print("DISCARD:", old_key[1])
        else:
            for i, k in enumerate(self.__lru):
                if k[1] == key:
                    self.__lru.pop(i)


        heappush(self.__lru, (self.__age, key))
        self.cache_data[key] = item
        self.__age += 1

    def get(self, key):
        """ Retrieve item from cache with specified key
        """
        if not key:
            return None
        item = self.cache_data.get(key, None)
        if not item:
            return None
        return item[1]


if __name__ == '__main__':
    my_cache = LRUCache()
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
