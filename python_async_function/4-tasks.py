#!/usr/bin/env python3
""" fifth async function """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """create a list of task"""
    if n < 1:
        return
    list_r = []
    for element in range(n):
        element = task_wait_random(max_delay)
        list_r.append(element)

    List_sort = await asyncio.gather(*list_r)

    return sorted(List_sort)
