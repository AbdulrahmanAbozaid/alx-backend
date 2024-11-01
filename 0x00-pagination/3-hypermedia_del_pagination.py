#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from pydoc import pager
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return page data with deletion-resilient pagination."""
        assert index is not None and\
            0 <= index < len(self.__indexed_dataset), "Index out of range."

        # Initialize pagination data
        data = []
        current_index = index
        dataset_len = len(self.__indexed_dataset)

        # Collect items for the current page, skipping missing entries
        while len(data) < page_size and current_index < dataset_len:
            if current_index in self.__indexed_dataset:
                data.append(self.__indexed_dataset[current_index])
            current_index += 1

        # Set next_index as the first available index after the current page
        next_index = current_index

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
