from src.hacker_rank.python.introduction.print_function import print_function


# https://www.hackerrank.com/challenges/python-print/problem
# noinspection SpellCheckingInspection
def test_print_function(capsys):  # noqa
    print_function(3)
    captured = capsys.readouterr()
    assert captured.out == "123\n"
