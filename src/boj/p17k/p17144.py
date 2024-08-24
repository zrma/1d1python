from itertools import product
from typing import NamedTuple, TextIO


class MoveParams(NamedTuple):
    y: int
    x: int
    dy: int
    dx: int
    limit_y: int
    limit_x: int


def solve17144(reader: TextIO, writer: TextIO) -> None:
    rows, cols, time = map(int, reader.readline().split())
    current_room = [list(map(int, reader.readline().split())) for _ in range(rows)]

    purifier_positions = [y for y in range(rows) if current_room[y][0] == -1]
    purifier_top_idx = purifier_positions[0]
    purifier_bottom_idx = purifier_positions[1]

    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def spread_dust(y: int, x: int, room: list[list[int]], new_room: list[list[int]]) -> None:
        amount = room[y][x] // 5
        spread_count = 0
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols and room[ny][nx] != -1:
                new_room[ny][nx] += amount
                spread_count += 1
        new_room[y][x] -= amount * spread_count

    def spread(room: list[list[int]]) -> list[list[int]]:
        new_room = [row[:] for row in room]
        for y, x in product(range(rows), range(cols)):
            if room[y][x] > 0:
                spread_dust(y, x, room, new_room)
        return new_room

    def move_purifier(room: list[list[int]], movements: list[MoveParams]) -> None:
        prev = 0
        for params in movements:
            y, x = params.y, params.x
            while (y != params.limit_y or params.dy == 0) and (x != params.limit_x or params.dx == 0):
                room[y][x], prev = prev, room[y][x]
                y += params.dy
                x += params.dx

    def purify(room: list[list[int]], top_idx: int, bottom_idx: int) -> None:
        cols_count, rows_count = len(room[0]), len(room)

        top_movements = [
            MoveParams(top_idx, 1, 0, 1, top_idx, cols_count - 1),  # 오른쪽
            MoveParams(top_idx, cols_count - 1, -1, 0, 0, cols_count - 1),  # 위쪽
            MoveParams(0, cols_count - 1, 0, -1, 0, 0),  # 왼쪽
            MoveParams(0, 0, 1, 0, top_idx, 0),  # 아래쪽
        ]

        bottom_movements = [
            MoveParams(bottom_idx, 1, 0, 1, bottom_idx, cols_count - 1),  # 오른쪽
            MoveParams(bottom_idx, cols_count - 1, 1, 0, rows_count - 1, cols_count - 1),  # 아래쪽
            MoveParams(rows_count - 1, cols_count - 1, 0, -1, rows_count - 1, 0),  # 왼쪽
            MoveParams(rows_count - 1, 0, -1, 0, bottom_idx, 0),  # 위쪽
        ]

        move_purifier(room, top_movements)
        move_purifier(room, bottom_movements)

    for _ in range(time):
        current_room = spread(current_room)
        purify(current_room, purifier_top_idx, purifier_bottom_idx)

    ans = sum(sum(cell for cell in row if cell > 0) for row in current_room)
    writer.write(f"{ans}")
