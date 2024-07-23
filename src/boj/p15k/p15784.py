from typing import Final, TextIO


def solve15784(reader: TextIO, writer: TextIO) -> None:
    n, y, x = map(int, reader.readline().split())
    charm_map = [list(map(int, reader.readline().split())) for _ in range(n)]

    y_idx: Final[int] = y - 1
    x_idx: Final[int] = x - 1

    charm = charm_map[y_idx][x_idx]
    row = charm_map[y_idx]
    col = (charm_map[i][x_idx] for i in range(n))

    ans = "ANGRY" if any(value > charm for value in row) or any(value > charm for value in col) else "HAPPY"

    writer.write(ans)
