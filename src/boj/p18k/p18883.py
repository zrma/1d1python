from typing import TextIO


def solve18883(reader: TextIO, writer: TextIO) -> None:
    n, m = map(int, reader.readline().split())
    result = "\n".join(" ".join(str(i * m + j + 1) for j in range(m)) for i in range(n))
    writer.write(f"{result}\n")
