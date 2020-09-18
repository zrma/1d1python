from itertools import product, combinations
from typing import Sequence


def mul_mat(mat1: Sequence[Sequence[int]], mat2: Sequence[Sequence[int]]) -> int:
    row = len(mat1)
    col = len(mat1[0])

    total = 0
    for x in range(row):
        for y in range(col):
            v1, v2 = mat1[x][y], mat2[y][x]
            if v2 == 1 and v1 == -1:
                raise ValueError
            total += v1 * v2
    return total


def build_mat(down_way: Sequence[bool], up_way: Sequence[bool], row: int, col: int):
    mat = [[0 for _ in range(row)] for _ in range(col)]

    mat[0][0] = 1
    pos_x, pos_y = 0, 0
    for step in down_way:
        if step:
            pos_x += 1
        else:
            pos_y += 1
        mat[pos_y][pos_x] = 1

    pos_x, pos_y = 0, 0
    for step in up_way:
        if step:
            pos_x += 1
        else:
            pos_y += 1
        mat[pos_y][pos_x] = 1

    return mat


def collect_max(mat: Sequence[Sequence[int]]):
    row = len(mat)
    col = len(mat[0])

    if mat[row - 1][col - 1] == -1:
        return 0

    row_step = row - 1
    col_step = col - 1
    total_step = row_step + col_step
    down_ways = [
        [True if x in y else False for x in range(total_step)]
        for y in [x for x in combinations(range(total_step), col_step)]
    ]
    up_ways = [
        [True if x in y else False for x in range(total_step)]
        for y in [x for x in combinations(range(total_step), col_step)]
    ]

    highest_score = 0

    for down_way, up_way in product(down_ways, up_ways):
        mat2 = build_mat(down_way, up_way, row, col)

        try:
            score = mul_mat(mat, mat2)
        except ValueError:
            continue

        highest_score = max(score, highest_score)

    return highest_score
