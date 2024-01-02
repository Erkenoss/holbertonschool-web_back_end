#!/usr/bin/env python3
""" sixth basic annotation """


def sum_list(input_list: float) -> float:
    """return the sum of number in a list"""
    sum: float = 0.0
    for element in input_list:
        sum += element
    return sum
