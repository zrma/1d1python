from threading import Thread

from src.leetcode.problems.lv_0_easy.print_in_order import Foo


def print_first(f: Foo):
    f.first(lambda: print("first", end=""))


def print_second(f: Foo):
    f.second(lambda: print("second", end=""))


def print_third(f: Foo):
    f.third(lambda: print("third", end=""))


# https://leetcode.com/problems/print-in-order/
def test_concurrent(capsys):  # noqa
    f = Foo()

    tasks = [
        Thread(target=print_first, args=(f,)),
        Thread(target=print_third, args=(f,)),
        Thread(target=print_second, args=(f,)),
    ]

    for task in tasks:
        task.start()

    for task in tasks:
        task.join()

    # noinspection SpellCheckingInspection
    expected = "firstsecondthird"

    captured = capsys.readouterr()
    assert captured.out == expected
