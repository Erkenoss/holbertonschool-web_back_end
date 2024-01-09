#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
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

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        return tuple (index 0 of page given and
        the number of element at the end of the page)
        """
        index = page - 1
        return index * page_size, page_size * page

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ return dict start on index of the current page """
        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        if index is None:
            index = 0

        assumed_page = (index // page_size) + 1
        start, end = self.index_range(assumed_page, page_size)

        next_index = end
        if next_index > len(self.dataset()):
            next_index = None

        dictionnary = {
            'index': start,
            'next_index': next_index,
            'page_size': page_size,
            'data': self.dataset()[start:end]
        }

        return dictionnary
