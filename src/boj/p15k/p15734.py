from typing import Final, TextIO


def solve15734(reader: TextIO, writer: TextIO) -> None:
    left, right, extra = map(int, reader.readline().split())

    diff: Final[int] = abs(left - right)
    if extra >= diff:
        extra -= diff
        left = right = max(left, right)
        left += extra // 2
        right += extra // 2
    else:
        if left < right:
            left += extra
        else:
            right += extra

    ans = min(left, right) * 2
    writer.write(f"{ans}")
