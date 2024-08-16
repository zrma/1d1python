from typing import TextIO


def solve19572(reader: TextIO, writer: TextIO) -> None:
    d1, d2, d3 = map(float, reader.readline().split())

    # a + b = d1 => (1)
    # a + c = d2 => (2)
    # b + c = d3 => (3)

    # (1) - (2) => b - c = d1 - d2 => (4)
    # (4) + (3) => 2b = d1 - d2 + d3 => (5)
    b = (d1 - d2 + d3) / 2
    a = d1 - b
    c = d2 - a

    result = f"1\n{a:.1f} {b:.1f} {c:.1f}" if a > 0 and b > 0 and c > 0 else "-1"
    writer.write(result)
