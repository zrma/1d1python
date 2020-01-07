from __future__ import annotations


class Player:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} {self.score}"

    @staticmethod
    def comparator(a: Player, b: Player) -> int:
        def cmp(lhs, rhs) -> int:
            return (lhs > rhs) - (lhs < rhs)

        cmp1 = cmp(b.score, a.score)
        if cmp1 == 0:
            return cmp(a.name, b.name)
        return cmp1
