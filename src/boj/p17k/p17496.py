from typing import Final, TextIO


def solve17496(reader: TextIO, writer: TextIO) -> None:
    n, t, c, p = map(int, reader.readline().split())

    harvests = (n - 1) // t
    ans: Final[int] = harvests * c * p

    writer.write(f"{ans}")
