#!/usr/bin/env python3
"""
Hypermedia pagination utility for a dataset of popular baby names.
"""

import csv
import math
from typing import Tuple, List, Dict, Any

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.
    
    :param page: The current page number.
    :param page_size: The number of items per page.
    :return: A tuple containing the start and end indices for the specified page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

class Server:
    """
    Server class to handle hypermedia pagination of a database containing popular baby names.
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
        
        :param page: The current page number.
        :param page_size: The number of items per page.
        :return: A list containing the data for the specified page.
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return dataset information as a dictionary with hypermedia pagination details.
        
        :param page: The current page number.
        :param page_size: The number of items per page.
        :return: A dictionary containing dataset information with pagination details.
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
