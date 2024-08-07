from copy import deepcopy
from itertools import product
from typing import Any, Callable, Sequence, Tuple


def find_the_runner_up_score(arr: Sequence[int]) -> int:
    return sorted(set(arr), reverse=True)[1]


def list_comprehensions(x: int, y: int, z: int, n: int) -> Sequence[Sequence[int]]:
    return [[a, b, c] for (a, b, c) in product(range(x + 1), range(y + 1), range(z + 1)) if a + b + c != n]


def nested_lists(arr: list[str | int | float]) -> Sequence[str]:
    if len(arr) == 0:
        return []

    names: list[Any] = arr[::2]
    scores: list[Any] = arr[1::2]
    result: list[Tuple[str, int | float]] = sorted(zip(names, scores), key=lambda x: x[1])

    def get_bottom(target: int | float) -> Sequence[str]:
        lst = []
        while result and result[0][1] == target:
            lst.append(result.pop(0)[0])
        return lst

    get_bottom(result[0][1])
    return sorted(get_bottom(result[0][1]))


def finding_the_percentage(query_name: str, student_marks: dict[str, Sequence[float]]) -> str:
    avg: float = 0
    try:
        arr = student_marks[query_name]
        avg = sum(arr) / len(arr)
    except (KeyError, ZeroDivisionError):
        pass

    return format(avg, ".2f")


def lists(commands: Sequence[Sequence[str]]) -> Sequence[Sequence[int]]:
    stack: list[int] = []
    result: list[Sequence[int]] = []

    operators: dict[str, Callable[[list[int]], int | None]] = {
        "insert": lambda x: stack.insert(x[0], x[1]),
        "remove": lambda x: stack.remove(x[0]),
        "append": lambda x: stack.append(x[0]),
        "sort": lambda _: stack.sort(),
        "pop": lambda _: stack.pop(-1),
        "reverse": lambda _: stack.reverse(),
        "print": lambda _: result.append(deepcopy(stack)),
    }

    for cmd in commands:
        op_code, *op_land = cmd
        operators[op_code](list(map(int, op_land)))

    return result


def tuples(arr: Sequence[int]) -> int:
    return hash(tuple(arr))
