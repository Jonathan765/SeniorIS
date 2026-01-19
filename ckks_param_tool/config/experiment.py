from dataclasses import dataclass
from typing import Optional
from dataclasses import asdict

@dataclass(frozen=True)
class DataConfig:
    num_samples: int
    method: str
    rounding: int
    test_size: float
    random_state: int

    def to_dict(self):
        return asdict(self)

@dataclass(frozen=True)
class EvaluationConfig:
    num_samples: int

    def to_dict(self):
        return asdict(self)

@dataclass(frozen=True)
class PlottingConfig:
    error_tol: Optional[float]

    def to_dict(self):
        return asdict(self)

@dataclass(frozen=True)
class SelectionConfig:
    objective: str

    def to_dict(self):
        return asdict(self)

@dataclass(frozen=True)
class ExperimentConfig:
    data: DataConfig
    evaluation: EvaluationConfig
    plotting: PlottingConfig
    selection: SelectionConfig

    def to_dict(self):
        return {
            "data": self.data.to_dict(),
            "evaluation": self.evaluation.to_dict(),
            "plotting": self.plotting.to_dict(),
            "selection": self.selection.to_dict(),
        }