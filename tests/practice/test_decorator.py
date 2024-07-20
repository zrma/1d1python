import pytest
from pytest import CaptureFixture

from src.practice.decorator import say_hello_with_decorator


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
