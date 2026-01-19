from abc import ABC, abstractmethod
from ckks_param_tool.params import CKKSParams
from .metrics import InferenceEvaluationResult

class InferenceEvaluator(ABC):

    @abstractmethod
    def evaluate(self) -> InferenceEvaluationResult:
        pass

