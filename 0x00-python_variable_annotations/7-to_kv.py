#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""


from typing import Dict, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ a type-annotated function to_kv"""
    result: Tuple[str, float] = (k, v * v)
    return result
