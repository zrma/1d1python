from threading import Event
from typing import Callable


class Foo:
    def __init__(self):
        self.e1 = Event()
        self.e2 = Event()

    def first(self, print_first: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        print_first()

        self.e1.set()

    def second(self, print_second: Callable[[], None]) -> None:
        self.e1.wait()

        # printSecond() outputs "second". Do not change or remove this line.
        print_second()

        self.e2.set()

    def third(self, print_third: Callable[[], None]) -> None:
        self.e2.wait()

        # printThird() outputs "third". Do not change or remove this line.
        print_third()
