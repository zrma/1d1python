from typing import TextIO


def solve20361(reader: TextIO, writer: TextIO) -> None:
    _, x, p = map(int, reader.readline().split())
    ans = x

    for _ in range(p):
        a, b = map(int, reader.readline().split())
        if ans in (a, b):
            ans = b if ans == a else a

    writer.write(f"{ans}")
