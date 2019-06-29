def if_else(n: int) -> None:
    weird = "Weird"
    not_weird = "Not Weird"

    if n % 2 is not 0:
        print(weird)
        return

    if 6 <= n <= 20:
        print(weird)
        return

    print(not_weird)
