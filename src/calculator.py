def parse(s: str) -> tuple:
    s = s.replace(' ', '')

    l_value = value = 0
    op = ''
    for c in s:
        if c.isdigit():
            value *= 10
            value += int(c)
        else:
            op = c
            l_value, value = value, 0

    return l_value, op, value
