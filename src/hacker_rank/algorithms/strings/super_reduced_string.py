from typing import List


def super_reduced_string(s: str) -> str:
    empty_string = "Empty String"

    if not s:
        return empty_string

    stack: List[str] = list()
    idx = -1

    for c in s:
        if idx >= 0 and stack[idx] == c:
            stack.pop(idx)
            idx -= 1
        else:
            stack.insert(idx + 1, c)
            idx += 1
    if not stack:
        return empty_string
    return ''.join(stack)
