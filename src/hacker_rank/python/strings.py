import textwrap
from itertools import product
from re import findall
from string import ascii_lowercase, capwords
from typing import Sequence


def swap_case(s: str) -> str:
    def change(c: str) -> str:
        if not c.isalpha():
            return c
        if c.isupper():
            return c.lower()
        return c.upper()

    return "".join(map(change, s))


def split_and_join(s: str) -> Sequence[str]:
    return s.replace(" ", "-")


def what_s_your_name(first: str, last: str) -> None:
    print(f"Hello {first} {last}! You just delved into python.")


def mutations(s: str, pos: int, c: str) -> str:
    return "".join((s[:pos], c, s[pos + 1 :]))


def count_substring(string: str, sub_string: str) -> int:
    return len(findall(f"(?={sub_string})", string))


def validate_string(s: str) -> None:
    print(any((x for x in s if x.isalnum())))
    print(any((x for x in s if x.isalpha())))
    print(any((x for x in s if x.isdigit())))
    print(any((x for x in s if x.islower())))
    print(any((x for x in s if x.isupper())))


def text_alignment(thickness: int, c: str) -> None:
    print()

    # Top Cone
    for i in range(thickness):
        left_margin = (c * i).rjust(thickness - 1)
        middle = c
        right_margin = (c * i).ljust(thickness - 1)

        s = left_margin + middle + right_margin
        print(f"{s}.")

    # Top Pillars
    for i in range(thickness + 1):
        left_pillar = (c * thickness).center(thickness * 2)
        right_pillar = (c * thickness).center(thickness * 6)

        s = left_pillar + right_pillar
        print(f"{s}.")

    # Middle Belt
    for i in range((thickness + 1) // 2):
        s = (c * thickness * 5).center(thickness * 6)
        print(f"{s}.")

        # Bottom Pillars
    for i in range(thickness + 1):
        left_pillar = (c * thickness).center(thickness * 2)
        right_pillar = (c * thickness).center(thickness * 6)

        s = left_pillar + right_pillar
        print(f"{s}.")

        # Bottom Cone
    for i in range(thickness):
        left_margin = (c * (thickness - i - 1)).rjust(thickness)
        middle = c
        right_margin = (c * (thickness - i - 1)).ljust(thickness)

        s = (left_margin + middle + right_margin).rjust(thickness * 6)
        print(f"{s}.")


def wrap(string: str, max_width: int) -> str:
    return "\n".join(textwrap.wrap(string, max_width))


def designer_door_mat(n: int, m: int) -> None:
    output: list[list[str]] = [["-" for _ in range(m)] for _ in range(n)]
    output[n // 2] = list("WELCOME".center(m, "-"))

    def point(pos_x: int, pos_y: int) -> None:
        output[pos_y][pos_x - 1] = "."
        output[pos_y][pos_x] = "|"
        output[pos_y][pos_x + 1] = "."

    center = m // 2
    for y in range(n):
        if y == n // 2:
            continue
        for offset in range(n // 2 - abs(n // 2 - y) + 1):
            point(center + offset * 3, y)
            point(center - offset * 3, y)

    for row in output:
        print("".join(row))


def print_formatted(number: int) -> None:
    length = len(str(bin(number))) - 2

    for i in range(1, number + 1):
        d = str(i).rjust(length)
        o = str(oct(i))[2:].rjust(length)
        h = str(hex(i))[2:].upper().rjust(length)
        b = str(bin(i))[2:].rjust(length)
        print(f"{d} {o} {h} {b}")


def print_pattern(size: int) -> None:
    center_x = (size - 1) * 2
    center_y = size - 1
    length = center_x * 2 + 1
    output: list[list[str]] = [["-" for _ in range(length)] for _ in range(size * 2 - 1)]

    def point(c: str, margin: int) -> None:
        # >>> [(i, j) for (i, j) in product(range(0, 2, 2),range(0, 1, 1))]
        # [(0, 0)]
        #
        # >>> [(i, j) for (i, j) in product(range(-2, 4, 2),range(-1, 2, 1))]
        # [(-2, -1), (-2, 0), (-2, 1),
        #  ( 0, -1), ( 0, 0), ( 0, 1),
        #  ( 2, -1), ( 2, 0), ( 2, 1)]
        #
        # >>> [(i, j) for (i, j) in product(range(-4, 6, 2),range(-2, 3, 1))]
        # [(-4, -2), (-4, -1), (-4, 0), (-4, 1), (-4, 2),
        #  (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2),
        #  ( 0, -2), ( 0, -1), ( 0, 0), ( 0, 1), ( 0, 2),
        #  ( 2, -2), ( 2, -1), ( 2, 0), ( 2, 1), ( 2, 2),
        #  ( 4, -2), ( 4, -1), ( 4, 0), ( 4, 1), ( 4, 2)]
        #
        # 일반화
        # >>> [(i, j) for (i, j) in product(range(-2k, 2(k+1), 2),range(-k, k+1, 1))]
        begin = range(-2 * margin, 2 * (margin + 1), 2)
        end = range(-margin, margin + 1, 1)
        for pos_x, pos_y in product(begin, end):
            if abs(pos_x) // 2 + abs(pos_y) == margin:
                output[center_y + pos_y][center_x + pos_x] = c

    for i in range(size):
        point(ascii_lowercase[i], i)

    for line in output:
        print("".join(line))


def capitalize(s: str) -> str:
    return capwords(s, " ")


def minion_game(s: str) -> None:
    vowels = "AEIOU"
    stuart, kevin = 0, 0

    for i, c in enumerate(s):
        # noinspection SpellCheckingInspection
        if c in vowels:
            # 문제의 그림에 나온 words 출력 순서에 속지 말자
            #
            # B          ┬
            # BA         │
            # BAN        │   BANANA
            # BANA       │   ├────┤
            # BANAN      │   B부터 BANANA까지 6개의 substring 포함
            # BANANA     ┴
            #
            #   N       ┬
            #   NA      │      NANA
            #   NAN     │      ├──┤
            #   NANA    ┴      N부터 NANA까지 4개의 substring 포함
            #
            #     N
            #     NA             N부터 NA까지 2개의 substring 포함
            kevin += len(s) - i
        else:
            stuart += len(s) - i

    if stuart > kevin:
        print(f"Stuart {stuart}")
        return
    if stuart < kevin:
        print(f"Kevin {kevin}")
        return
    print("Draw")


def merge_the_tools(s: str, k: int) -> None:
    for begin, end in zip(range(0, len(s), k), range(k, len(s) + 1, k)):
        result = ""
        token = s[begin:end]
        for t in token:
            if t not in result:
                result += t

        print(result)
