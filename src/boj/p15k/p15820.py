from typing import Final, TextIO


def solve15820(reader: TextIO, writer: TextIO) -> None:
    sample_num, sys_num = map(int, reader.readline().split())

    def is_correct(num_cases: int) -> bool:
        return all(map(lambda x: x[0] == x[1], (tuple(map(int, reader.readline().split())) for _ in range(num_cases))))

    samples: Final[bool] = is_correct(sample_num)
    systems: Final[bool] = is_correct(sys_num)

    result = {
        (True, True): "Accepted",
        (True, False): "Why Wrong!!!",
        (False, True): "Wrong Answer",
        (False, False): "Wrong Answer",
    }[(samples, systems)]

    writer.write(result)
