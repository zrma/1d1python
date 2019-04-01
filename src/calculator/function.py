from typing import Union, List, Optional


def calc(_: str) -> Union[int, float]:
    # _: List[str] = parse(s)

    result: Union[int, float] = 0
    return result


def get_inner_bracket(l: List[Union[str, int]]) -> List[Union[str, int]]:
    start = 0
    end = len(l)
    if ")" in l:
        end = l.index(")")
        start = 0
        for i, c in enumerate(l[0:end]):
            if c == "(":
                start = i + 1
        return l[start:end]

    return l[start:end]


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
