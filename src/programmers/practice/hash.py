from collections import Counter
from typing import Sequence


def incomplete_players(participant: Sequence[str], completion: Sequence[str]) -> str:
    try:
        return next((Counter(participant) - Counter(completion)).elements())
    except StopIteration:
        raise ValueError(f"Invalid arguments: {participant} {completion}")


def phone_number_startswith(phone_book: Sequence[str]) -> bool:
    phone_book = sorted(phone_book)
    for first, second in zip(phone_book, phone_book[1:]):
        if second.startswith(first):
            return False
    return True
