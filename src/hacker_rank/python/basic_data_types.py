from typing import Sequence


def find_the_runner_up_score(arr: Sequence[int]) -> int:
    return sorted(set(arr), reverse=True)[1]
