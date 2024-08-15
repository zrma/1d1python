from typing import Final, TextIO


def solve18856(reader: TextIO, writer: TextIO) -> None:
    n: Final[int] = int(reader.readline())

    ans = " ".join(map(str, (*range(1, n), 997)))

    writer.write(f"{n}\n{ans}")
