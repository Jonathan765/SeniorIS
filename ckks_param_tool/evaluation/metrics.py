from dataclasses import dataclass, asdict

'''
This file contains the classes that represent the metrics obtained during parameter evaluation
and inference evaluation.
'''

@dataclass
class ParameterEvaluationResult:
    error: float # plaintext-ciphertext error
    runtime: float # average encrypted inference runtime across test vectors
    security_bits: float # security level of the chosen parameters
    status: str # was backend encryption success or failure
    failure_reason: str = "" # if failure, what was the reason
             
@dataclass
class InferenceEvaluationResult:
    error: float # plaintext-ciphertext error
    runtime: float # one-time encrypted inference runtime

    def to_dict(self): # used for output
        return asdict(self)