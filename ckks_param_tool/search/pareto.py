import numpy as np
import pandas as pd

'''
This file contains the functions that define the Pareto frontier logic.
'''

# this function computes a dataframe mask that identifies the pareto optimal parameters
def pareto_mask(
    df: pd.DataFrame,
    metrics: list[str],
) -> pd.Series:

    values = df[metrics].to_numpy()
    n = values.shape[0]

    is_pareto = np.ones(n, dtype=bool)

    for i in range(n):
        if not is_pareto[i]:
            continue

        # defines the dominate relation
        dominates = (
            np.all(values <= values[i], axis=1)
            & np.any(values < values[i], axis=1)
        )
        dominates[i] = False

        if np.any(dominates):
            is_pareto[i] = False

    return pd.Series(is_pareto, index=df.index)

# this is a wrapper function that returns the pareto optimal rows of the results dataframe
def pareto_rows(
    df: pd.DataFrame,
    metrics: list[str],
) -> pd.DataFrame:
    mask = pareto_mask(df, metrics)
    return df[mask].copy()

# this function selects the "knee" point of the frontier to recommend, but this can be changed if
# a given objective is deemed more important, such as error or runtime, through a 'policy' parameter
def select_representative_pareto(
    pareto_df: pd.DataFrame,
    policy: str = "knee",
) -> pd.Series:

    if len(pareto_df) == 1:
        return pareto_df.iloc[0]

    if policy == "fastest":
        return pareto_df.loc[pareto_df["runtime"].idxmin()]

    if policy == "most_accurate":
        return pareto_df.loc[pareto_df["max_err"].idxmin()]

    # calculating the knee point logic as the default
    rt = pareto_df["runtime"]
    err = pareto_df["max_err"]

    if rt.max() == rt.min() or err.max() == err.min():
        return pareto_df.loc[rt.idxmin()]

    rt_norm = (rt - rt.min()) / (rt.max() - rt.min())
    err_norm = (err - err.min()) / (err.max() - err.min())

    score = rt_norm + err_norm
    return pareto_df.loc[score.idxmin()]