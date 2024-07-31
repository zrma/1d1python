from typing import Final, TextIO


def solve16503(reader: TextIO, writer: TextIO) -> None:
    k1, op1, k2, op2, k3 = reader.readline().split()

    a: Final[int] = int(k1)
    b: Final[int] = int(k2)
    c: Final[int] = int(k3)

    def operate(op: str, lhs: int, rhs: int) -> int:
        match op:
            case "+":
                return lhs + rhs
            case "-":
                return lhs - rhs
            case "*":
                return lhs * rhs
            case _:
                if lhs * rhs < 0:
                    return -(abs(lhs) // abs(rhs))
                else:
                    return lhs // rhs

    result1 = operate(op1, a, operate(op2, b, c))
    result2 = operate(op2, operate(op1, a, b), c)

    writer.write(f"{min(result1, result2)}\n{max(result1, result2)}")
