from typing import Final, TextIO


def solve23348(reader: TextIO, writer: TextIO) -> None:
    a, b, c = map(int, reader.readline().split())
    num_teams: Final[int] = int(reader.readline().strip())

    def team_score() -> int:
        return sum(a * x + b * y + c * z for x, y, z in (map(int, reader.readline().split()) for _ in range(3)))

    ans = max(team_score() for _ in range(num_teams))

    writer.write(f"{ans}")
