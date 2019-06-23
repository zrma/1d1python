from sys import maxsize
from typing import Iterable

INT_MAX = maxsize
INT_MIN = -maxsize - 1


def array_manipulation(n: int, queries: Iterable[Iterable[int]]) -> int:
    arr = [0 for _ in range(n + 1)]
    for row in queries:
        begin, end, value = row  # type: int
        arr[begin - 1] += value
        arr[end] -= value

    result = INT_MIN
    cur = 0
    for num in arr:
        cur += num
        result = max(result, cur)

    return result
