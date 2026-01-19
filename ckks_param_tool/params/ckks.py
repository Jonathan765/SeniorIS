from dataclasses import dataclass
from .security import calculate_security_score

@dataclass(frozen=True)
class CKKSParams:
    poly_degree: int
    scale: int
    chain: tuple[int, ...]

    @property
    def chain_sum(self) -> int:
        return sum(self.chain)
    
    @property
    def security_score(self) -> float:
        return calculate_security_score(self.poly_degree, self.chain_sum)
    
   