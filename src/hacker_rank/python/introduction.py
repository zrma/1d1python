def arithmetic_operators(a: int, b: int) -> None:
    print(a + b)
    print(a - b)
    print(a * b)


def division(a: int, b: int) -> None:
    print(a // b)
    print(a / b)


def hello_world() -> None:
    print("Hello, World!")


def if_else(n: int) -> None:
    weird = "Weird"
    not_weird = "Not Weird"

    if n % 2 != 0:
        print(weird)
        return

    if 6 <= n <= 20:
        print(weird)
        return

    print(not_weird)


def loops(n: int) -> None:
    for i in range(n):
        print(i ** 2)


def print_function(n: int) -> None:
    print("".join((str(x) for x in range(1, n + 1))))


def is_leap(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True

    return False
