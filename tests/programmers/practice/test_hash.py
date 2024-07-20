from typing import Sequence

import attrs
import pytest

from src.programmers.practice.hash import incomplete_players, phone_number_startswith


def test_incomplete_players() -> None:
    """
    https://programmers.co.kr/learn/courses/30/lessons/42576
    완주하지 못한 선수
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        participant: Sequence[str]
        completion: Sequence[str]
        want: str

    # noinspection SpellCheckingInspection
    test_cases = (
        TestCase(participant=["leo", "kiki", "eden"], completion=["eden", "kiki"], want="leo"),
        TestCase(
            participant=["marina", "josipa", "nikola", "vinko", "filipa"],
            completion=["josipa", "filipa", "marina", "nikola"],
            want="vinko",
        ),
        TestCase(
            participant=["mislav", "stanko", "mislav", "ana"], completion=["stanko", "ana", "mislav"], want="mislav"
        ),
    )

    for tt in test_cases:
        got = incomplete_players(tt.participant, tt.completion)
        assert got == tt.want


def test_incomplete_players_error() -> None:
    with pytest.raises(ValueError, match=r"Invalid arguments: \[\] \[\]"):
        incomplete_players([], [])


def test_phone_number_startswith() -> None:
    """
    https://programmers.co.kr/learn/courses/30/lessons/42577
    전화번호 목록
    """

    @attrs.frozen(auto_attribs=True, kw_only=True)
    class TestCase:
        phone_book: Sequence[str]
        want: bool

    for tt in (
        TestCase(phone_book=["119", "97674223", "1195524421"], want=False),
        TestCase(phone_book=["1195524421", "97674223", "119"], want=False),
        TestCase(phone_book=["123", "456", "789"], want=True),
        TestCase(phone_book=["12", "123", "1235", "567", "88"], want=False),
    ):
        got = phone_number_startswith(tt.phone_book)
        assert got == tt.want
