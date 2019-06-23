from sys import maxsize
from typing import Sequence

INT_MAX = maxsize
INT_MIN = -maxsize - 1


def hourglass_sum(arr: Sequence[Sequence[int]]) -> int:
    row_size = len(arr)
    if row_size < 3:
        return 0

    col_size = len(arr[0])
    if col_size < 3:
        return 0

    def calc(_x, _y: int) -> int:
        total = arr[_y - 1][_x - 1] + arr[_y - 1][_x] + arr[_y - 1][_x + 1]
        total += arr[_y][_x]
        total += arr[_y + 1][_x - 1] + arr[_y + 1][_x] + arr[_y + 1][_x + 1]
        return total

    max_val = INT_MIN
    for y in range(1, row_size - 1):
        for x in range(1, col_size - 1):
            val = calc(x, y)
            max_val = max(max_val, val)

    return max_val
