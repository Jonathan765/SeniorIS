from abc import ABC, abstractmethod
from ckks_param_tool.params import CKKSParams
from .metrics import ParameterEvaluationResult

'''
This file contains the abstract parameter evaluation class.
'''
class ParameterEvaluator(ABC):

    @abstractmethod
    def evaluate(self, params: CKKSParams) -> ParameterEvaluationResult:
        pass

