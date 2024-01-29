#!/usr/bin/env python3
"""
Simple pagination for a dataset of popular baby names.
"""

import csv
from typing import List, Tuple

class Server:
    """
    Server class to handle pagination of a database containing popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server instance with an empty dataset.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieve the dataset, reading from the CSV file if not already cached.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of the dataset based on pagination parameters.
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        csv_size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, csv_size)

        if start >= csv_size:
            return []

        return self.dataset()[start:end]

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.
    """
    return ((page - 1) * page_size, page * page_size)
