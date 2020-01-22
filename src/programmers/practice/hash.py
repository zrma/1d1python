from collections import Counter
from typing import Sequence


def incomplete_players(participant: Sequence[str], completion: Sequence[str]) -> str:
    return ','.join(list((Counter(participant) - Counter(completion)).elements()))
