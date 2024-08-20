from typing import TextIO


def solve21866(reader: TextIO, writer: TextIO) -> None:
    scores = list(map(int, reader.readline().split()))

    max_scores = [100, 100, 200, 200, 300, 300, 400, 400, 500]

    if any(score > max_score for score, max_score in zip(scores, max_scores)):
        writer.write("hacker")
    elif sum(scores) >= 100:
        writer.write("draw")
    else:
        writer.write("none")
