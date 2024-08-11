from math import sqrt
from typing import TextIO


def solve17945(reader: TextIO, writer: TextIO) -> None:
    b, c = map(int, reader.readline().split())

    # Solve the quadratic equation: x^2 + 2bx + c = 0
    # Using the quadratic formula:
    # x = (-2b ± sqrt((2b)^2 - 4 * 1 * c)) / 2
    # x = (-2b ± sqrt(4b^2 - 4c)) / 2
    # x = -b ± sqrt(b^2 - c)

    discriminant = b**2 - c
    sqrt_discriminant = int(sqrt(discriminant))

    x1 = -b + sqrt_discriminant
    x2 = -b - sqrt_discriminant

    if x1 == x2:
        writer.write(f"{x1}")
    else:
        writer.write(f"{min(x1, x2)} {max(x1, x2)}")
