from itertools import islice
from typing import Final, Iterator, TextIO


def solve15781(reader: TextIO, writer: TextIO) -> None:
    n, m = map(int, reader.readline().split())

    helmets: Final[Iterator[int]] = map(int, reader.readline().split())
    vests: Final[Iterator[int]] = map(int, reader.readline().split())

    max_helmets: Final[int] = max(islice(helmets, n))
    max_vests: Final[int] = max(islice(vests, m))

    result: Final[int] = max_helmets + max_vests
    writer.write(f"{result}")
