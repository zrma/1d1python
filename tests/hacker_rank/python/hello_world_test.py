from src.hacker_rank.python.hello_world import hello_world


# https://www.hackerrank.com/challenges/py-hello-world/problem
# noinspection SpellCheckingInspection
def test_print_test(capsys):  # noqa
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
