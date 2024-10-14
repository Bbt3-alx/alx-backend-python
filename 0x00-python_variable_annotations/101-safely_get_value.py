#!/usr/bin/env python3
"""More involved type annotations"""


from typing import Mapping, Any, Union


def safely_get_value(dct: Mapping, key: Any, default: Union[~T, None]) -> dict:
    """involved type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
