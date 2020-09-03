from collections import namedtuple

from src.programmers.practice.hash import incomplete_players, phone_number_startswith


# https://programmers.co.kr/learn/courses/30/lessons/42576
def test_incomplete_players():
    case = namedtuple("TestCase", "participant completion expected")

    # noinspection SpellCheckingInspection
    cases = (
        case(participant=["leo", "kiki", "eden"],
             completion=["eden", "kiki"],
             expected="leo"),
        case(participant=["marina", "josipa", "nikola", "vinko", "filipa"],
             completion=["josipa", "filipa", "marina", "nikola"],
             expected="vinko"),
        case(participant=["mislav", "stanko", "mislav", "ana"],
             completion=["stanko", "ana", "mislav"],
             expected="mislav"),
    )

    for case in cases:
        assert case.expected == incomplete_players(case.participant, case.completion)


# https://programmers.co.kr/learn/courses/30/lessons/42577
def test_phone_number_startswith():
    case = namedtuple("TestCase", "phone_book expected")

    cases = (
        case(phone_book=["119", "97674223", "1195524421"], expected=False),
        case(phone_book=["123", "456", "789"], expected=True),
        case(phone_book=["12", "123", "1235", "567", "88"], expected=False),
    )

    for case in cases:
        assert case.expected == phone_number_startswith(case.phone_book)
