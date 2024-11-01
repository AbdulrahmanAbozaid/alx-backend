#!/usr/bin/env python3
"""
Simple helper function
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """The function should return a tuple of size two containing a start
    index and an end index corresponding to the range of indexes to return in a
    list for those particular pagination parameters.

    Args:
        page (int): page number.
        page_size (int): page size

    Returns:
        tuple: 2-sized tuple
    """
    offset = (page - 1) * page_size
    return (offset, offset + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert (isinstance(page, int) and page > 0)
        assert (isinstance(page_size, int) and page_size > 0)
        data = self.dataset()
        total_items = len(data)

        if (page > ((total_items + page_size - 1) // page_size)
                or (page_size > total_items and page > 1)):
            return []
        indecies = index_range(page, page_size)
        return data[indecies[0]:indecies[1]]
