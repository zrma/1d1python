from typing import List, Sequence


def rot_left(a: List[int], d: int) -> Sequence[int]:
    length = len(a)

    if d < 1 or d % length == 0:
        return a

    if d > length:
        d = d % length

    return a[d:] + a[:d]
