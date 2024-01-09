#!/usr/bin/env python3
""" class server """
import csv
import math
from typing import List


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = self.index_range(page, page_size)

        if start >= len(self.dataset) or end >= len(self.dataset):
            return []

        return self.dataset[start:end + 1]





    def index_range(page: int, page_size: int) -> tuple:
        """
        return tuple (index 0 of page given and
        the number of element at the end of the page)
        """
        index = page - 1
        return index * page_size, page_size * page
