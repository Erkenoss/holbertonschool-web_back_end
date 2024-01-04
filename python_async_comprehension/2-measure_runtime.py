#!/usr/bin/env python3
""" measure time of execution """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return time execution"""
    start = time.time()

    loop = [async_comprehension() for numb in range(4)]
    await asyncio.gather(*loop)

    end = time.time()
    return end - start
