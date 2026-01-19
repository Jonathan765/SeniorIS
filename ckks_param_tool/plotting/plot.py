import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ckks_param_tool.config import PlottingConfig

def plot_precision_vs_security(df: pd.DataFrame, config: PlottingConfig):
    
    df_success = df
    error_tol = config.error_tol

    if error_tol:
        df_success = df_success[df_success["max_err"] < error_tol]

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.scatter(
        df_success["max_err"],
        df_success["security"],
        alpha=0.7,
        s=50
    )

    ax.set_xscale("log")
    ax.set_xlabel("Max Absolute Error")
    ax.set_ylabel("Estimated Security (bits)")
    ax.set_title("Security vs Precision")
    ax.grid(True, which="both", ls="--", lw=0.5)

    fig.tight_layout()
    return fig

def plot_runtime_vs_precision(df: pd.DataFrame, config: PlottingConfig):
    df_success = df
    error_tol = config.error_tol

    if error_tol is not None:
        df_success = df_success[df_success["max_err"] < error_tol]

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.scatter(
        df_success["max_err"],
        df_success["runtime"],
        alpha=0.7,
        s=50
    )

    ax.set_xscale("log")
    ax.set_xlabel("Max Absolute Error")
    ax.set_ylabel("Runtime (s)")
    ax.set_title("Runtime vs Precision")
    ax.grid(True, which="both", ls="--", lw=0.5)

    fig.tight_layout()
    return fig
    
def plot_runtime_vs_security(df: pd.DataFrame, config: PlottingConfig):
    df_success = df
    error_tol = config.error_tol

    if error_tol is not None:
        df_success = df_success[df_success["max_err"] < error_tol]

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.scatter(
        df_success["runtime"],
        df_success["security"],
        alpha=0.7,
        s=50
    )

    ax.set_xlabel("Runtime (s)")
    ax.set_ylabel("Estimated Security (bits)")
    ax.set_title("Security vs Runtime")
    ax.grid(True, which="both", ls="--", lw=0.5)

    fig.tight_layout()
    return fig