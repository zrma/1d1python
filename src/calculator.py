def parse(s: str) -> tuple:
    s = s.replace(' ', '')

    val1 = val2 = 0
    op = ''
    for c in s:
        if c.isdigit():
            val2 *= 10
            val2 += int(c)
        else:
            op = c
            val1, val2 = val2, 0

    return op, val1, val2


def eval(t: tuple) -> (int or float):
    pass
