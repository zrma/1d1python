from functools import cmp_to_key
from typing import TextIO


def solve21312(reader: TextIO, writer: TextIO) -> None:
    a, b, c = map(int, reader.readline().split())

    combi = [a, b, c, a * b, b * c, c * a, a * b * c]

    def compare(x: int, y: int) -> int:
        if x % 2 == y % 2:
            return x - y
        return x % 2 - y % 2

    ans = sorted(combi, key=cmp_to_key(compare), reverse=True)[0]
    writer.write(f"{ans}")
