from typing import Final, TextIO


def solve17618(reader: TextIO, writer: TextIO) -> None:
    n: Final[int] = int(reader.readline().strip())

    result = 0
    for i in range(1, n + 1):
        x = i
        digit_sum = 0
        while x > 0:
            digit_sum += x % 10
            x //= 10
        if i % digit_sum == 0:
            result += 1

    writer.write(f"{result}")
