#!/usr/bin/env python3
""" second async function """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """create a list of random"""
    if n < 1: 
        return
    list_r = []
    for element in range(n):
        list_r.append(wait_random(max_delay))
        # element = wait_random(max_delay)
        # list_r.append(element)

    List_sort = await asyncio.gather(*list_r)

    return sorted(List_sort)
