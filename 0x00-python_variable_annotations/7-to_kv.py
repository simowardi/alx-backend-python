#!/usr/bin/env python3
"""
Defines a function that returns a tuple with a string and the square of a number.

Args:
    k (str): A string value.
    v (union[int, float]): An integer or float value.

Returns:
    tuple[str, float]: A tuple with the input string and the square of the input number.
"""

from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v ** 2)
