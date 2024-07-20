from pytest import CaptureFixture

from src.utils.print import print_test


def test_print_test(capsys: CaptureFixture[str]) -> None:
    print_test()
    captured = capsys.readouterr()
    assert captured.out == "hello world\n"
