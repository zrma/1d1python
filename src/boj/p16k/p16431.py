from typing import Final, TextIO


def solve16431(reader: TextIO, writer: TextIO) -> None:
    br, bc = map(int, reader.readline().split())
    dr, dc = map(int, reader.readline().split())
    jr, jc = map(int, reader.readline().split())

    bessie_dist: Final[int] = max(abs(jr - br), abs(jc - bc))
    daisy_dist: Final[int] = abs(jr - dr) + abs(jc - dc)

    if bessie_dist < daisy_dist:
        writer.write("bessie")
        return
    if bessie_dist > daisy_dist:
        writer.write("daisy")
        return
    writer.write("tie")
