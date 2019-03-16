from typing import Union, List


def add_bracket(s: str) -> str:
    s = s.replace(' ', '')
    return s


def calc(s: str) -> Union[int, float]:
    l: List[str] = list()
    result: Union[int, float] = 0

    s = add_bracket(s)
    return result
