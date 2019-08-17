from src.hacker_rank.python.strings import *


class TestStrings:
    # noinspection SpellCheckingInspection
    # https://www.hackerrank.com/challenges/swap-case/problem
    def test_swap_case(self):
        assert swap_case("Www.HackerRank.com") == "wWW.hACKERrANK.COM"
        assert swap_case("Pythonist 2") == "pYTHONIST 2"
        assert swap_case('HackerRank.com presents "Pythonist 2".') \
               == 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'

    # https://www.hackerrank.com/challenges/python-string-split-and-join/problem
    def test_split_and_join(self):
        assert split_and_join("this is a string") == "this-is-a-string"

    # https://www.hackerrank.com/challenges/whats-your-name/problem
    # noinspection SpellCheckingInspection
    def test_what_s_your_name(self, capsys):  # noqa
        what_s_your_name("Ross", "Taylor")
        captured = capsys.readouterr()
        assert captured.out == "Hello Ross Taylor! You just delved into python.\n"

    # https://www.hackerrank.com/challenges/python-mutations/problem
    def test_mutations(self):
        # noinspection SpellCheckingInspection
        assert mutations("abracadabra", 5, "k") == "abrackdabra"

    # https://www.hackerrank.com/challenges/find-a-string/problem
    def test_count_substring(self):
        # noinspection SpellCheckingInspection
        assert count_substring("ABCDCDC", "CDC") == 2

    # https://www.hackerrank.com/challenges/string-validators/problem
    # noinspection SpellCheckingInspection
    def test_validate_string(self, capsys):  # noqa
        validate_string("qA2")
        captured = capsys.readouterr()
        assert captured.out == "True\nTrue\nTrue\nTrue\nTrue\n"
