#!/usr/bin/env python3
""" duck type an iterable object"""


from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """duck type an iterable object"""
    return [(i, len(i)) for i in lst]
