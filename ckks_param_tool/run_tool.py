import numpy as np

from encryption.tenseal_backend import TenSEALBackend
from tool.evaluation.tenseal_evaluator import TenSEALEvaluator
from tool.types import CKKSParams
from tool.search_space import CKKSParameterSearchSpace
from tool.selection.constraints import CKKSConstraints
from tool.selection.objective import ErrorObjective
from tool.selection.tenseal_selector import CKKSParameterSelector

from tool.plotting.plotting import plot_precision_vs_security
from tool.plotting.plotting import plot_runtime_vs_precision
from tool.plotting.plotting import plot_runtime_vs_security
from tool.plotting.plotting import results_to_dataframe
import pandas as pd

def toy_model(x):
    return x * 2

def test_tenseal_evaluator_basic():
    
    params = CKKSParams(
        poly_degree=8192,
        scale=2**40,
        chain=(60, 40, 60)
    )
    backend = TenSEALBackend(params)

    test_vectors = [
        np.array([1.0, 2.0, 3.0]),
        np.array([0.5, -1.0, 4.0])
    ]

    evaluator = TenSEALEvaluator(
        backend=backend,
        model=toy_model,
        test_vectors=test_vectors
    )

    result = evaluator.evaluate()

    print("Evaluation result:", result)


def test_selector():
    test_vectors = [
        np.array([1.0, 2.0, 3.0]),
        np.array([0.5, -1.0, 4.0]),
        np.array([2.0, 0.0, -1.0]),
    ]

    evaluator = TenSEALEvaluator(
        backend=TenSEALBackend,
        model=toy_model,
        test_vectors=test_vectors
    )

    selector = CKKSParameterSelector(
        evaluator=evaluator,
        search_space=CKKSParameterSearchSpace(1),
        constraints=None,
        objective=ErrorObjective()
    )

    results = selector.select()

    best = results[0]
    print("\n🏆 BEST PARAMS:")
    print(best[0])
    print(best[1])

    return results

res = test_selector()

df = results_to_dataframe(res)

plot_precision_vs_security(df)
plot_runtime_vs_precision(df)
plot_runtime_vs_security(df)


   