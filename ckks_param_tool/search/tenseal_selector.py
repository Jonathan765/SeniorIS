import pandas as pd
from .selector import ParameterSelector
from ckks_param_tool.plotting import results_to_dataframe
from .pareto import (
    pareto_mask,
    select_representative_pareto
)

'''
This file contains the class that defines the searching and selection of parameters using TenSEAL
'''

class CKKSParameterSelector(ParameterSelector):
    def __init__(self, evaluator, search_space):
        self.evaluator = evaluator # how to evaluate a parameter set
        self.search_space = search_space # how to generate candidates
        self.results = None

    # this function generates the candidate parameters and evaluates them
    def select(self):
        results = []
        for params in self.search_space.generate():

            result = self.evaluator.evaluate(params)
            results.append((params, result))

        self.results = sorted(results, key=lambda x: x[1].error) # sort by error for the output

        return self.results

    # this function applies the Pareto logic to the results
    def get_pareto_optimal_params(self):
        df = results_to_dataframe(self.results)

        # Initializing new columns
        df["is_pareto"] = False 
        df["is_recommended"] = False

        for sec in (128, 192, 256):
            subset = df[df["security"] == sec]

            if subset.empty:
                continue

            # calculate the Pareto-optimal points across runtime and error
            mask = pareto_mask(
                subset,
                metrics=["runtime", "max_err"]
            )

            df.loc[subset.index, "is_pareto"] = mask

            pareto_df = subset[mask]

            if pareto_df.empty:
                continue

            # apply the knee point logic
            rep = select_representative_pareto(pareto_df)

            df.loc[rep.name, "is_recommended"] = True

        pareto_indices = df.index[df["is_pareto"]].tolist()
        recommended_indices = df.index[df["is_recommended"]].tolist()

        return {
            "pareto": [self.results[i] for i in pareto_indices],
            "recommended": [self.results[i] for i in recommended_indices],
            "df": df
        }