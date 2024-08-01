#!/usr/bin/env python3

"""
Defines a function that returns the sum of a mixed list of integers and floats.

Args:
    mxd_lst (list[union[int, float]]): A list of integers and floats.

Returns:
    float: The sum of the input list of integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
