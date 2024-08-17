from itertools import islice
from typing import Final, List, TextIO


def solve20053(reader: TextIO, writer: TextIO) -> None:
    t: Final[int] = int(reader.readline())

    def read_n_values(n: int) -> List[int]:
        return list(islice(map(int, reader.readline().split()), n))

    ans = (f"{min(arr)} {max(arr)}" for _ in range(t) if (arr := read_n_values(int(reader.readline()))))

    writer.write("\n".join(ans))
