from typing import Final, TextIO


def solve15953(reader: TextIO, writer: TextIO) -> None:
    t: Final[int] = int(reader.readline().strip())

    ans = []
    for _ in range(t):
        a, b = map(int, reader.readline().split())
        prize = get_first_prize(a) + get_second_prize(b)
        ans.append(str(prize))

    writer.write("\n".join(ans))


def get_first_prize(a: int) -> int:
    if a == 1:
        return 5000000
    if 2 <= a <= 3:
        return 3000000
    if 4 <= a <= 6:
        return 2000000
    if 7 <= a <= 10:
        return 500000
    if 11 <= a <= 15:
        return 300000
    if 16 <= a <= 21:
        return 100000
    return 0


def get_second_prize(b: int) -> int:
    if b == 1:
        return 5120000
    if 2 <= b <= 3:
        return 2560000
    if 4 <= b <= 7:
        return 1280000
    if 8 <= b <= 15:
        return 640000
    if 16 <= b <= 31:
        return 320000
    return 0
