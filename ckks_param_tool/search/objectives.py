from abc import ABC, abstractmethod

class Objective(ABC):
    
    @abstractmethod
    def score(self, result):
        pass

class RuntimeObjective(Objective):
    def score(self, result):
        return result.runtime

class ErrorObjective(Objective):
    def score(self, result):
        return result.error

class WeightedObjective(Objective):
    def __init__(self, alpha=1.0, beta=1.0):
        self.alpha = alpha
        self.beta = beta

    def score(self, result):
        return (
            self.alpha * result.runtime +
            self.beta * result.error
        )

_OBJECTIVES = {
    "weighted": WeightedObjective,
    "error": ErrorObjective,
    "runtime": RuntimeObjective,
}

def get_objective(objective: str) -> Objective:
    
    if objective not in _OBJECTIVES:
        raise ValueError(f"Unknown objective '{objective}'")

    return _OBJECTIVES[objective]()


