import json
from .experiment import (
    ExperimentConfig,
    DataConfig,
    EvaluationConfig,
    PlottingConfig,
    SelectionConfig,
)

def load_experiment_config(path: str) -> ExperimentConfig:
    with open(path) as f:
        raw = json.load(f)

    return ExperimentConfig(
        data=DataConfig(**raw["data"]),
        evaluation=EvaluationConfig(**raw["evaluation"]),
        plotting=PlottingConfig(**raw["plotting"]),
        selection=SelectionConfig(**raw["selection"]),
    )