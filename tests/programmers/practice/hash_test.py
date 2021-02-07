from dataclasses import dataclass
from typing import Sequence

from src.programmers.practice.hash import incomplete_players, phone_number_startswith


# https://programmers.co.kr/learn/courses/30/lessons/42576
def test_incomplete_players():
    @dataclass
    class Case:
        participant: Sequence[str]
        completion: Sequence[str]
        expected: str

    # noinspection SpellCheckingInspection
    cases = (
        Case(participant=["leo", "kiki", "eden"],
             completion=["eden", "kiki"],
             expected="leo"),
        Case(participant=["marina", "josipa", "nikola", "vinko", "filipa"],
             completion=["josipa", "filipa", "marina", "nikola"],
             expected="vinko"),
        Case(participant=["mislav", "stanko", "mislav", "ana"],
             completion=["stanko", "ana", "mislav"],
             expected="mislav"),
    )

    for case in cases:
        assert case.expected == incomplete_players(case.participant, case.completion)


# https://programmers.co.kr/learn/courses/30/lessons/42577
def test_phone_number_startswith():
    @dataclass
    class Case:
        phone_book: Sequence[str]
        expected: bool

    cases = (
        Case(phone_book=["119", "97674223", "1195524421"], expected=False),
        Case(phone_book=["1195524421", "97674223", "119"], expected=False),
        Case(phone_book=["123", "456", "789"], expected=True),
        Case(phone_book=["12", "123", "1235", "567", "88"], expected=False),
    )

    for case in cases:
        assert case.expected == phone_number_startswith(case.phone_book)
