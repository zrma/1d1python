from typing import TextIO


def solve18127(reader: TextIO, writer: TextIO) -> None:
    a, b = map(int, reader.readline().split())

    #   b: 0   1   2   3   4   5   6
    # a=3: 1  +2 + 3 + 4 + 5 + 6 + 7
    # a=4: 1  +3 + 5 + 7 + 9 +11 +13
    # a=5: 1  +4 + 7 +10 +13 +16 +19
    # a=6: 1  +5 + 9 +13 +17 +21 +25
    # a=7: 1  +6 +11 +16 +21 +26 +31

    # The difference between consecutive terms in the arithmetic sequence
    diff = a - 2

    # Number of terms in the sequence: n = b + 1
    num_terms = b + 1

    # Sum of the arithmetic sequence:
    # S = n * (2 * a + (n - 1) * diff) // 2
    # Where n is the number of terms, and diff is the common difference
    ans = num_terms * (2 + b * diff) // 2

    writer.write(f"{ans}")
