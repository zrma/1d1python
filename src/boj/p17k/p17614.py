from typing import Final, TextIO


def solve17614(reader: TextIO, writer: TextIO) -> None:
    n: Final[int] = int(reader.readline().strip())

    target_digits = {3, 6, 9}

    def count_3_6_9(x: int) -> int:
        count = 0
        while x > 0:
            if x % 10 in target_digits:
                count += 1
            x //= 10
        return count

    result = sum(count_3_6_9(i) for i in range(1, n + 1))

    writer.write(f"{result}")
