from functools import cmp_to_key

from pytest import CaptureFixture

from src.hacker_rank.interview_preparation_kit.sorting.comparator import Player


def test_comparator(capsys: CaptureFixture[str]) -> None:
    """
    https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem
    Sorting: Comparator
    """
    # noinspection SpellCheckingInspection
    give = (
        Player.from_tuple(t) for t in (("amy", 100), ("david", 100), ("heraldo", 50), ("aakansha", 75), ("aleksa", 150))
    )
    sorted_players = sorted(give, key=cmp_to_key(Player.comparator))
    for p in sorted_players:
        print(p.name, p.score)

    # noinspection SpellCheckingInspection
    want = """aleksa 150
amy 100
david 100
aakansha 75
heraldo 50
"""
    captured = capsys.readouterr()
    assert captured.out == want


def test_player_repr() -> None:  # noqa
    give = Player(name="test", score=123)
    want = """Player(name='test', score=123)"""
    assert repr(give) == want
