from functools import lru_cache

cache = {}


def fibonacci_cached(number: int) -> int:
    if number in cache:
        return cache[number]
    if number == 0 or number == 1:
        return number
    else:
        result = fibonacci_cached(number - 2) + fibonacci_cached(number - 1)
        cache[number] = result
        return result


@lru_cache(maxsize=256)
def fibonacci_lru_cached(number: int) -> int:
    if number == 0 or number == 1:
        return number
    else:
        return fibonacci_lru_cached(number - 2) + fibonacci_lru_cached(number - 1)
