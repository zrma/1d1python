from itertools import count, takewhile
from typing import TextIO


def solve17174(reader: TextIO, writer: TextIO) -> None:
    n, m = map(int, reader.readline().split())

    result = sum(takewhile(lambda x: x > 0, (n // (m**i) for i in count())))

    writer.write(f"{result}")
