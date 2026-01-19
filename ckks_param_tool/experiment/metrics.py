from dataclasses import dataclass
from ckks_param_tool.params import CKKSParams
from ckks_param_tool.evaluation import InferenceEvaluationResult

@dataclass
class ExperimentResult:
    param_search_results: list
    best_params: CKKSParams
    inference_result: InferenceEvaluationResult