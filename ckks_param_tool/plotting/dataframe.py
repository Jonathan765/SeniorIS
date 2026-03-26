import pandas as pd

'''
This file contains a helper function for the plotting functionality. It turns the dictionary
output into a structured dataframe.
'''
def results_to_dataframe(results):
    rows = []

    for result in results:
        params = result[0]
        metrics = result[1]

        rows.append({
            "poly_degree": params.poly_degree,
            "scale": params.scale,
            "chain": params.chain,
            "chain_sum": sum(params.chain),
            "depth": len(params.chain),
            "max_err": metrics.error,
            "runtime": metrics.runtime,
            "security": metrics.security_bits,
            "total_memory": params.memory["total"],
            "status": metrics.status,
            "failure_reason": metrics.failure_reason
        })

    return pd.DataFrame(rows)