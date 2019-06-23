from collections import namedtuple

from src.hacker_rank.solve.frequency import frequency

Case = namedtuple("TestCase", "input expected desc")


def test_frequency():
    cases = (
        Case(input="1226#24#",
             expected="1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1",
             desc="# 처리 실패"),
        Case(input="1(2)23(3)",
             expected="2 1 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
             desc="괄호 처리 실패"),
        Case(input="2110#(2)",
             expected="1 1 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
             desc="# + 괄호 처리 실패"),
        Case(input="23#(2)24#25#26#23#(3)",
             expected='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 5 1 1 1',
             desc="복잡한 형태의 # + 괄호 중복 복합 처리 실패"),
        Case(input="26#24#12",
             expected="1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1",
             desc="# 포함하지만 큰 수로 끝나지 않는 경우의 처리 실패"),
    )

    for case in cases:
        assert case.expected == ' '.join([str(s) for s in frequency(case.input)]), case.desc
