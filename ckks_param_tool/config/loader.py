import json
from .experiment import (
    ExperimentConfig,
    DataConfig,
    EvaluationConfig,
    PlottingConfig,
)
from .defaults import DEFAULT_EXPERIMENT_CONFIG
from pathlib import Path

'''
This file contains the function that parses an input file location into a correct Config object.
'''
def load_experiment_config(config=None) -> ExperimentConfig:
    
    if config is None:
        return DEFAULT_EXPERIMENT_CONFIG
    
    if isinstance(config, (str, Path)):

        path = Path(config)

        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")

        with open(path) as f:
            raw = json.load(f)

        required_sections = {"data", "evaluation", "plotting", "selection"}
        missing = required_sections - raw.keys()
        if missing:
            raise KeyError(f"Missing config sections: {missing}")

        return ExperimentConfig(
            data=DataConfig(**raw["data"]),
            evaluation=EvaluationConfig(**raw["evaluation"]),
            plotting=PlottingConfig(**raw["plotting"]),
        )

    raise TypeError(
        "config must be None or a path."
    )