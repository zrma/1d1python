from typing import Final, TextIO


def solve16504(reader: TextIO, writer: TextIO) -> None:
    n: Final[int] = int(reader.readline().strip())

    total_sum: Final[int] = sum(sum(map(int, reader.readline().split())) for _ in range(n))

    writer.write(f"{total_sum}")
