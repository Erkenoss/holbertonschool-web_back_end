#!/usr/bin/env python3
""" random 10 times and return this random """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ generate and yield random """
    for i in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
