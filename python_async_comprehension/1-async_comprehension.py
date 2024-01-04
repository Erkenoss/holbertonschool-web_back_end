#!/usr/bin/env python3
"""  """
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    rand_x_ten = [numb async for numb in async_generator()]
    return rand_x_ten
