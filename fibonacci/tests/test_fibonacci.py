from typing import Callable

from fibonacci.dynamic import fibonacci_dynamic
from fibonacci.naive import fibonacci_naive
from fibonacci.cached import fibonacci_cached, fibonacci_lru_cached
import pytest


@pytest.mark.parametrize(
    "func", [fibonacci_naive, fibonacci_cached, fibonacci_lru_cached, fibonacci_dynamic]
)
@pytest.mark.parametrize("number, expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_fibonacci(time_tracker, func: Callable, number: int, expected: int) -> None:
    actual = func(number)
    assert actual == expected
