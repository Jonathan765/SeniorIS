from dataclasses import dataclass, asdict

@dataclass
class ParameterEvaluationResult:
    error: float
    runtime: float
    security_bits: float

    
           
@dataclass
class InferenceEvaluationResult:
    error: float
    runtime: float

    def to_dict(self):
        return asdict(self)