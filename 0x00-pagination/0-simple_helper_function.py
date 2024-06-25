#!/usr/bin/env python3
"""Module for the page indexing function
"""


def index_range(page: int, page_size: int) -> tuple:
    """Page indexing function
    """
    return (page_size * (page - 1), page_size * page)


if __name__ == '__main__':
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
