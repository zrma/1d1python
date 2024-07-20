from __future__ import annotations

import attrs


@attrs.frozen(auto_attribs=True, kw_only=True)
class Player:
    name: str
    score: int

    @classmethod
    def from_tuple(cls, t: tuple[str, int]) -> Player:
        return cls(name=t[0], score=t[1])

    @staticmethod
    def comparator(a: Player, b: Player) -> int:
        if a.score == b.score:
            return (a.name > b.name) - (a.name < b.name)
        return (b.score > a.score) - (b.score < a.score)
