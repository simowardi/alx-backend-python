#!/usr/bin/env python3

"""
Defines a function that takes an iterable object and returns a list of tuples
containing the original element and its length.

Args:
    lst (typing.Iterable[typing.Sequence]): An iterable object of sequences.

Returns:
    typing.List[typing.Tuple[typing.Sequence, int]]: A list of tuples, where the
    first element of each tuple is the original sequence from the input iterable,
    and the second element is the length of that sequence.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
