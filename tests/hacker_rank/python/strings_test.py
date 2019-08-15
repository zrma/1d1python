from src.hacker_rank.python.strings import *


class TestStrings:
    # noinspection SpellCheckingInspection
    # https://www.hackerrank.com/challenges/swap-case/problem
    def test_swap_case(self):
        assert swap_case("Www.HackerRank.com") == "wWW.hACKERrANK.COM"
        assert swap_case("Pythonist 2") == "pYTHONIST 2"
        assert swap_case('HackerRank.com presents "Pythonist 2".') \
               == 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'
