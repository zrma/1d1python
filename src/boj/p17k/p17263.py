from itertools import islice
from typing import Final, TextIO


def solve17263(reader: TextIO, writer: TextIO) -> None:
    n: Final[int] = int(reader.readline().strip())
    max_val: Final[int] = max(islice(map(int, reader.readline().split()), n))
    writer.write(f"{max_val}")
