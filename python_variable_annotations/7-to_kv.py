#!/usr/bin/env python3
""" sixth basic annotation """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, int or float]:
    """tuple of two element"""
    return k, (v * v)
