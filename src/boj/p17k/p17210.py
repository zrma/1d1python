from typing import Final, TextIO


def solve17210(reader: TextIO, writer: TextIO) -> None:
    num_doors: Final[int] = int(reader.readline().strip())
    starting_state: Final[int] = int(reader.readline().strip())

    if num_doors > 5:
        writer.write("Love is open door")
        return

    door_states = (starting_state ^ i % 2 for i in range(1, num_doors))

    writer.write("\n".join(map(str, door_states)))
