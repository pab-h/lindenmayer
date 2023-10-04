from lindenmayer import Rule

from typing import Generator
from typing import Self

class Lindenmayer:
    def __init__(self, axiom: str, rules: list[Rule]):
        self.axiom = axiom
        self.dict_rules = { r.symbol: r.replacement for r in rules }
        self.last_interact = axiom

    def reset(self) -> None: 
        self.last_interact = self.axiom

    def apply(self) -> str:
        current_interact = ""

        for symbol in self.last_interact: 
            current_interact += self.dict_rules.get(symbol, symbol)

        self.last_interact = current_interact

        return self.last_interact
        
    def applyn(self, n) -> Generator[str, None, None]:
        for _ in range(n):
            yield self.apply()

    def __iter__(self) -> Self:
        return self
    
    def __next__(self) -> str: 
        return self.apply()