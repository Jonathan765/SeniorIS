from dataclasses import dataclass
from ckks_param_tool.params import CKKSParams
from ckks_param_tool.evaluation import InferenceEvaluationResult

'''
This file contains the class that outlines the results of running the tool.
'''

@dataclass
class ExperimentResult:

    # a list of candidate parameters and their evaluated metrics
    param_search_results: list 

    # a list of params that are Parto-optimal
    pareto_params: list[CKKSParams] 

    # a list of the recommended params and their associated real inference evaluation
    recommended_params: list[tuple[CKKSParams, InferenceEvaluationResult]] 