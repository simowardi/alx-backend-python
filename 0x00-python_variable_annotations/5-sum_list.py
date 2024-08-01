#!/usr/bin/env python3

"""
Defines a function that returns the sum of a list of floats.

Args:
    input_list (list[float]): A list of float values.

Returns:
    float: The sum of the input list of floats.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
