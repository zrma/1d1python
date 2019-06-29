def super_reduced_string(s: str) -> str:
    empty_string = "Empty String"

    if not s:
        return empty_string

    pair = [f"{c}{c}" for c in set(s)]

    def find() -> (str, bool):
        for c in pair:
            if c in s:
                return c, True
        return "", False

    c, ok = find()
    while ok:
        s = s.replace(c, "")
        c, ok = find()

    if not s:
        return empty_string
    return s
