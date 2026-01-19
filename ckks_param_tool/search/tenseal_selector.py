from .selector import ParameterSelector
from ckks_param_tool.config import SelectionConfig
from .objectives import get_objective

class CKKSParameterSelector(ParameterSelector):
    def __init__(self, evaluator, search_space, config: SelectionConfig):
        self.evaluator = evaluator
        self.search_space = search_space
        self.objective = get_objective(config.objective)

    def select(self):
        results = []

        for params in self.search_space.generate():

            result = self.evaluator.evaluate(params)

            score = self.objective.score(result)
            results.append((params, result, score))

        return sorted(results, key=lambda x: x[2])
