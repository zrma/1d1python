from typing import Final, TextIO


def solve15921(reader: TextIO, writer: TextIO) -> None:
    n: Final[int] = int(reader.readline().strip())
    if n == 0:
        writer.write("divide by zero")
        return

    tot: Final[int] = sum(map(int, reader.readline().split()))
    if tot == 0:
        writer.write("divide by zero")
        return

    writer.write("1.00")
