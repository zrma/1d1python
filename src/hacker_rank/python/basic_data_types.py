from itertools import product
from typing import Sequence, Union, Dict


def find_the_runner_up_score(arr: Sequence[int]) -> int:
    return sorted(set(arr), reverse=True)[1]


def list_comprehensions(x: int, y: int, z: int, n: int) -> Sequence[Sequence[int]]:
    return [
        [a, b, c] for (a, b, c) in product(range(x + 1), range(y + 1), range(z + 1))
        if a + b + c != n
    ]


def nested_lists(arr: Sequence[Union[int, str]]) -> Sequence[str]:
    if len(arr) == 0:
        return []

    names = arr[::2]
    scores = arr[1::2]
    result = sorted(zip(names, scores), key=lambda x: x[1])

    def get_bottom(target: float) -> Sequence[str]:
        lst = []
        while result and result[0][1] == target:
            lst.append(result.pop(0)[0])
        return lst

    get_bottom(result[0][1])
    return sorted(get_bottom(result[0][1]))


def finding_the_percentage(query_name: str, student_marks: Dict[str, Sequence[float]]) -> str:
    avg: float = 0
    try:
        arr = student_marks[query_name]
        avg = sum(arr) / len(arr)
    except (KeyError, ZeroDivisionError):
        pass

    return format(avg, '.2f')
