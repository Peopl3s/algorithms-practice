from typing import Dict
from functools import lru_cache

def fibonacci_iter(n: int) -> int:
    if n <= 1:
        return n
    fib_series = [0] * (n + 1)
    fib_series[0] = 0
    fib_series[1] = 1
    for i in range(2, n + 1):
        fib_series[i] = fib_series[i - 2] + fib_series[i - 1]
    return fib_series[n]


def fibonacci_simple(n:int) -> int:
    if n <= 1:
        return n
    return fibonacci_simple(n - 2) + fibonacci_simple(n - 1)
    
    
def fibonacci_memo(n: int, cache: Dict[int, int]) -> int:
    if not cache.get(n):
        if n <= 1:
            cache[n] = n
        else:
            cache[n] = (
                fibonacci_memo(n - 2, cache)
                + fibonacci_memo(n - 1, cache)
            )
    return cache[n]


@lru_cache(maxsize = 1000)
def fibonacci_lru(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_simple(n - 2) + fibonacci_simple(n - 1)
    

if __name__ == '__main__':
    print(fibonacci_simple(10))
    print(fibonacci_iter(10))
    print(fibonacci_memo(10, {}))
    print(fibonacci_lru(10))
    