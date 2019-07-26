from src.hacker_rank.python.loops import loops


# https://www.hackerrank.com/challenges/python-loops/problem
# noinspection SpellCheckingInspection
def test_loops(capsys):  # noqa
    loops(5)
    captured = capsys.readouterr()
    assert captured.out == f"0\n1\n4\n9\n16\n"
