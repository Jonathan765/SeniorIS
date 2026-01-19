import pandas as pd

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
            "score": result[2],
        })

    return pd.DataFrame(rows)