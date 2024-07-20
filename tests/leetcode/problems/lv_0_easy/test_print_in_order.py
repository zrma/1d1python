from threading import Thread

from pytest import CaptureFixture

from src.leetcode.problems.lv_0_easy.print_in_order import Foo


def print_first(f: Foo) -> None:
    f.first(lambda: print("first", end=""))


def print_second(f: Foo) -> None:
    f.second(lambda: print("second", end=""))


def print_third(f: Foo) -> None:
    f.third(lambda: print("third", end=""))


def test_concurrent(capsys: CaptureFixture[str]) -> None:
    """
    https://leetcode.com/problems/print-in-order/
    1114. Print in Order
    """
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
    want = "firstsecondthird"
    got = capsys.readouterr().out
    assert got == want
