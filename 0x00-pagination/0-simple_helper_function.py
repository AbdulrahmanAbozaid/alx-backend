#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """The function should return a tuple of size two
    containing a start index and an end index corresponding
    to the range of indexes to return in a
    list for those particular pagination parameters.

    Args:
        page (int): page number.
        page_size (int): page size

    Returns:
        tuple: 2-sized tuple
    """
    offset = (page - 1) * page_size
    return (offset, offset + page_size)
