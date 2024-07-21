import math
from typing import Final, TextIO


def solve15667(reader: TextIO, writer: TextIO) -> None:
    n: Final[int] = int(reader.readline().strip())

    def check(x: int) -> int:
        return 1 + x + x**2

    ans = 1
    while check(ans) < n:
        ans += 1

    writer.write(f"{ans}")


def solve15667_sqrt(reader: TextIO, writer: TextIO) -> None:
    n = int(reader.readline().strip())

    k = int(math.sqrt(n))
    writer.write(f"{k}")
