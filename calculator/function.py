from typing import Union, List, Optional


def add_bracket(s: str) -> str:
    s = s.replace(' ', '')
    return s


def calc(s: str) -> Union[int, float]:
    l: List[str] = list()
    result: Union[int, float] = 0

    s = add_bracket(s)
    return result


def parse(s: str) -> List[str]:
    s = s.replace(' ', '')

    result: List[Union[str, int]] = []
    num: Optional[int] = None
    for c in s:
        if c.isdigit():
            if num is not None:
                num *= 10
                num += int(c)
            else:
                num = int(c)
        else:
            if num is not None:
                result.extend((num, c))
            else:
                result.append(c)
            num = None
    if num is not None:
        result.append(num)

    return result
