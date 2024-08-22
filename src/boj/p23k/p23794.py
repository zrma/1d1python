from typing import Final, TextIO


def solve23794(reader: TextIO, writer: TextIO) -> None:
    n: Final[int] = int(reader.readline().strip())

    # Define the border line and middle line pattern
    border_line: Final[str] = "@" * (n + 2)
    middle_line: Final[str] = f"@{' ' * n}@"

    # Write the top border
    writer.write(f"{border_line}\n")

    # Write the middle lines
    writer.write(f"{middle_line}\n" * n)

    # Write the bottom border
    writer.write(border_line)
