#!/usr/bin/env python3
"""
Simple pagination helper function
"""

from typing import Tuple

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
