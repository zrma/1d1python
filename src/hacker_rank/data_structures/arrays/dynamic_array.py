from typing import Sequence, List


def dynamic_array(n: int, queries: Sequence[Sequence[int]]) -> Sequence[int]:
    result = []  # type: List[int]
    seq_list = [[] for _ in range(n)]  # type: List[List[int]]
    last_answer = 0
    for query in queries:
        cmd, x, y = query  # type: int
        if cmd == 1:
            seq_idx = (x ^ last_answer) % n
            seq = seq_list[seq_idx]
            seq.append(y)
        else:
            seq_idx = (x ^ last_answer) % n
            seq = seq_list[seq_idx]
            elem_idx = y % len(seq)
            last_answer = seq[elem_idx]  # type: int
            result.append(last_answer)

    return result
