from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, data: str):
        self.__data = data
        self.__left: Optional[Node] = None
        self.__right: Optional[Node] = None
