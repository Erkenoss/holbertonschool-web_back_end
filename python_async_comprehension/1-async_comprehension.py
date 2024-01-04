#!/usr/bin/env python3
""" use async for """
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ return a list of number random generate """
    rand_x_ten = [numb async for numb in async_generator()]
    return rand_x_ten
