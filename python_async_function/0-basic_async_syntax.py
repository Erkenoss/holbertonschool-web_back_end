#!/usr/bin/env python3
""" first async function """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait the random time"""
    random_value = random.random() * max_delay
    await asyncio.sleep(random_value)
    return random_value
