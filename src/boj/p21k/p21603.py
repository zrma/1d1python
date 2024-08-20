from typing import Final, TextIO


def solve21603(reader: TextIO, writer: TextIO) -> None:
    n, k = map(int, reader.readline().split())

    k_mod_10: Final[int] = k % 10
    double_k_mod_10: Final[int] = (2 * k) % 10

    ans = [x for x in range(1, n + 1) if (x_mod_10 := x % 10) != k_mod_10 and x_mod_10 != double_k_mod_10]

    writer.write(f"{len(ans)}")
    if ans:
        writer.write("\n" + " ".join(map(str, ans)))
