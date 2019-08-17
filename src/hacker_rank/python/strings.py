from typing import Sequence
from re import findall


def swap_case(s: str) -> str:
    def change(c: str) -> str:
        if not c.isalpha():
            return c
        if c.isupper():
            return c.lower()
        return c.upper()

    return ''.join(map(change, s))


def split_and_join(s: str) -> Sequence[str]:
    return s.replace(' ', '-')


def what_s_your_name(a: str, b: str):
    print(f"Hello {a} {b}! You just delved into python.")


def mutations(s: str, pos: int, c: str) -> str:
    return "".join((s[:pos], c, s[pos + 1:]))


def count_substring(string: str, sub_string: str) -> int:
    return len(findall(f"(?={sub_string})", string))


def validate_string(s: str):
    print(any((x for x in s if x.isalnum())))
    print(any((x for x in s if x.isalpha())))
    print(any((x for x in s if x.isdigit())))
    print(any((x for x in s if x.islower())))
    print(any((x for x in s if x.isupper())))


def text_alignment(thickness: int, c: str):
    print()

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

        # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

        # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c +
               (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
