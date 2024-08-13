from typing import Final, Generator, TextIO


def solve18247(reader: TextIO, writer: TextIO) -> None:
    t: Final[int] = int(reader.readline().strip())

    ans: Generator[str, None, None] = (
        "-1" if n < 12 or m < 4 else f"{m * 11 + 4}" for n, m in (map(int, reader.readline().split()) for _ in range(t))
    )

    writer.write("\n".join(ans))
