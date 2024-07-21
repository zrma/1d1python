from typing import Final, Iterator, TextIO


def solve15780(reader: TextIO, writer: TextIO) -> None:
    n, _ = map(int, reader.readline().split())
    sockets: Final[Iterator[int]] = map(int, reader.readline().split())

    usable_sockets: Final[int] = sum(socket // 2 + socket % 2 for socket in sockets)
    ans: Final[str] = "YES" if usable_sockets >= n else "NO"

    writer.write(ans)
