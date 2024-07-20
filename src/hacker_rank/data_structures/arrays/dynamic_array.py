from typing import Sequence, Tuple


def dynamic_array(n: int, queries: Sequence[Tuple[int, int, int]]) -> Sequence[int]:
    result: list[int] = []
    seq_list: list[list[int]] = [[] for _ in range(n)]
    last_answer = 0
    for query in queries:
        cmd, x, y = query
        if cmd == 1:
            seq_idx = (x ^ last_answer) % n
            seq = seq_list[seq_idx]
            seq.append(y)
        else:
            seq_idx = (x ^ last_answer) % n
            seq = seq_list[seq_idx]
            elem_idx = y % len(seq)
            last_answer = seq[elem_idx]
            result.append(last_answer)

    return result
