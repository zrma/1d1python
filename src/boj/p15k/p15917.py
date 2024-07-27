from typing import Final, TextIO


def solve15917(reader: TextIO, writer: TextIO) -> None:
    num_case: Final[int] = int(reader.readline().strip())

    def read_int() -> int:
        return int(reader.readline().strip())

    def is_power_of_two(x: int) -> bool:
        return x > 0 and (x & (x - 1)) == 0

    results = ("1" if is_power_of_two(read_int()) else "0" for _ in range(num_case))
    writer.write("\n".join(results))
