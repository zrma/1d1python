EMPTY_STRING = "Empty String"


def super_reduced_string(s: str) -> str:
    unique = set(s)
    if not unique:
        return EMPTY_STRING

    pair = [f"{c}{c}" for c in unique]

    def find() -> (bool, str):
        for c in pair:
            if c in s:
                return True, c
        return False, ""

    ok, c = find()
    while ok:
        s = s.replace(c, "")
        ok, c = find()

    if not s:
        return EMPTY_STRING
    return s
