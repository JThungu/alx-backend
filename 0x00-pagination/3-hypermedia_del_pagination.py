#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination utility for a dataset of popular baby names.
"""

import csv
from typing import List, Dict

class Server:
    """
    Server class to handle deletion-resilient hypermedia pagination of a database containing popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server instance with an empty dataset and an indexed dataset.
        """
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Retrieve an indexed version of the dataset by sorting position, starting at 0.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with key-value pairs (index, next_index, page_size, data).
        
        :param index: The starting index for pagination.
        :param page_size: The number of items per page.
        :return: A dictionary containing pagination details.
        """
        assert type(index) == int
        assert type(page_size) == int
        csv = self.indexed_dataset()
        csv_size = len(csv)
        assert 0 <= index < csv_size
        data = []
        _next = index
        for _ in range(page_size):
            while not csv.get(_next):
                _next += 1
            data.append(csv.get(_next))
            _next += 1
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": _next
        }

