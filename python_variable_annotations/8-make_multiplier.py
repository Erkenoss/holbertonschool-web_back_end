#!/usr/bin/env python3
""" sixth basic annotation """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ the square of a float """
    return lambda x: multiplier * x
