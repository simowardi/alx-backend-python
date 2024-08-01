#!/usr/bin/env python3
"""
Defines a function that returns a function that multiplies a float by a given multiplier.

Args:
    multiplier (float): The number to multiply floats by.

Returns:
    typing.Callable[[float], float]: A function that takes a float and returns the product of the float and the multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(number: float) -> float:
        return number * multiplier
    return multiply
