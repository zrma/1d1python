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
    elif 2 <= a <= 3:
        return 3000000
    elif 4 <= a <= 6:
        return 2000000
    elif 7 <= a <= 10:
        return 500000
    elif 11 <= a <= 15:
        return 300000
    elif 16 <= a <= 21:
        return 100000
    else:
        return 0


def get_second_prize(b: int) -> int:
    if b == 1:
        return 5120000
    elif 2 <= b <= 3:
        return 2560000
    elif 4 <= b <= 7:
        return 1280000
    elif 8 <= b <= 15:
        return 640000
    elif 16 <= b <= 31:
        return 320000
    else:
        return 0
