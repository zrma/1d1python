from typing import TextIO


def solve16673(reader: TextIO, writer: TextIO) -> None:
    c, k, p = map(int, reader.readline().split())

    total_wine_cost = sum(k * i + p * i**2 for i in range(1, c + 1))

    writer.write(f"{total_wine_cost}")
