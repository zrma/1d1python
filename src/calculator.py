def parse(s: str) -> tuple:
    lv, op, rv = s.split()
    return int(lv), op, int(rv)
