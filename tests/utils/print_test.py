from src.utils.print import print_test


# noinspection SpellCheckingInspection
def test_print_test(capsys):  # noqa
    print_test()
    captured = capsys.readouterr()
    assert captured.out == "hello world\n"
