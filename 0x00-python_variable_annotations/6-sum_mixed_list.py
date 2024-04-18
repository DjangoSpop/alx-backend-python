#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list (mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of all elements in a list of floats and integers."""
    return sum(mxd_lst)