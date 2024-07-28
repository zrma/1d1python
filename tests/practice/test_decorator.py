import pytest
from pytest import CaptureFixture

from src.practice.decorator import say_hello_list, say_hello_with_decorator


def test_say_hello_with_decorator(capsys: CaptureFixture[str]) -> None:
    say_hello_with_decorator("Boris")

    want = """decorator start: say_hello_with_decorator ('Boris',) {}
greeting, Boris!
decorator end: say_hello_with_decorator
"""
    got = capsys.readouterr().out
    assert got == want


def test_say_hello_with_decorator_invalid_call() -> None:
    with pytest.raises(ValueError, match=r"Invalid arguments: \('Foo', 'Bar'\) \{'last': 'Baz'\}"):
        say_hello_with_decorator("Foo", "Bar", last="Baz")


def test_say_hello_with_decorator_args(capsys: CaptureFixture[str]) -> None:
    say_hello_with_decorator("Alice")

    want = """decorator start: say_hello_with_decorator ('Alice',) {}
greeting, Alice!
decorator end: say_hello_with_decorator
"""
    got = capsys.readouterr().out
    assert got == want


def test_say_hello_list(capsys: CaptureFixture[str]) -> None:
    say_hello_list("Alice", 123)

    want = """decorator start: say_hello_list (123,) {}
got name='Alice'
greeting, i=0 s='Alice'!
n=123
decorator end: say_hello_list
"""
    got = capsys.readouterr().out
    assert got == want

    say_hello_list(3, 456)

    want = """decorator start: say_hello_list (456,) {}
got name=3
greeting, i=0 s='unknown'!
greeting, i=1 s='unknown'!
greeting, i=2 s='unknown'!
n=456
decorator end: say_hello_list
"""
    got = capsys.readouterr().out
    assert got == want
