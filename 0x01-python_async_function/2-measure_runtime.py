#!/usr/bin/env python3

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n.
    '''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
