from collections import Counter
from typing import Sequence


def incomplete_players(participant: Sequence[str], completion: Sequence[str]) -> str:
    return ','.join(list((Counter(participant) - Counter(completion)).elements()))


def phone_number_startswith(phone_book: Sequence[str]) -> bool:
    for idx, elem in enumerate(phone_book):
        if any(x.startswith(elem) for x in phone_book[:idx]):
            return False
        if any(x.startswith(elem) for x in phone_book[idx + 1:]):
            return False
    return True
