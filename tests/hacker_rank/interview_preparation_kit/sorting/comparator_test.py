from collections import namedtuple
from functools import cmp_to_key
from typing import List

from src.hacker_rank.interview_preparation_kit.sorting.comparator import Player

Case = namedtuple("TestCase", "n expected")


# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem
# noinspection SpellCheckingInspection
def test_comparator(capsys):  # noqa
    data = []
    for datum in (
            ("amy", 100),
            ("david", 100),
            ("heraldo", 50),
            ("aakansha", 75),
            ("aleksa", 150),
    ):
        name, score = datum
        score = int(score)
        player = Player(name, score)
        data.append(player)

    data = sorted(data, key=cmp_to_key(Player.comparator))
    for datum in data:
        print(datum.name, datum.score)

    expected = """aleksa 150
amy 100
david 100
aakansha 75
heraldo 50
"""
    captured = capsys.readouterr()
    assert captured.out == expected
