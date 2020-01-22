from collections import namedtuple
from typing import Sequence

from src.programmers.practice.hash import incomplete_players

Case = namedtuple("TestCase", "participant completion expected")


# https://programmers.co.kr/learn/courses/30/lessons/42576
def test_incomplete_players():
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
