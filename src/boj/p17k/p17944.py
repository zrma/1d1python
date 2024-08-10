from typing import Final, TextIO


def solve17944(reader: TextIO, writer: TextIO) -> None:
    n, t = map(int, reader.readline().split())

    cycle_length: Final[int] = 4 * n - 2
    position_in_cycle = t % cycle_length or cycle_length

    if position_in_cycle <= 2 * n:
        ans = position_in_cycle
    else:
        ans = 4 * n - position_in_cycle

    writer.write(f"{ans}")
