from typing import Sequence
from itertools import product


def find_the_runner_up_score(arr: Sequence[int]) -> int:
    return sorted(set(arr), reverse=True)[1]


def list_comprehensions(x: int, y: int, z: int, n: int) -> Sequence[Sequence[int]]:
    return [
        [a, b, c] for (a, b, c) in product(range(x + 1), range(y + 1), range(z + 1))
        if a + b + c != n
    ]
