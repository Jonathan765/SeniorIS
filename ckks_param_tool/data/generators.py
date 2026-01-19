import numpy as np
from scipy.stats import truncnorm
from ckks_param_tool.config import DataConfig

def _compute_feature_descriptors(X):
    return {
        "mean": np.mean(X, axis=0),
        "std": np.std(X, axis=0),
        "min": np.min(X, axis=0),
        "max": np.max(X, axis=0),
    }

def _sample_truncated_normal(descriptors, n_samples, rng):
    mean = descriptors["mean"]
    std = descriptors["std"]
    min_val = descriptors["min"]
    max_val = descriptors["max"]

    a = (min_val - mean) / std
    b = (max_val - mean) / std

    samples = truncnorm.rvs(
        a, b,
        loc=mean,
        scale=std,
        size=(n_samples, len(mean)),
        random_state=rng
    )

    return samples

def _sample_gaussian(descriptors, n_samples, rng):
    return rng.normal(
        loc=descriptors["mean"],
        scale=descriptors["std"],
        size=(n_samples, len(descriptors["mean"]))
    )

def _sample_uniform(descriptors, n_samples, rng):
    return rng.uniform(
        low=descriptors["min"],
        high=descriptors["max"],
        size=(n_samples, len(descriptors["min"]))
    )

_SAMPLERS = {
    "truncated_normal": _sample_truncated_normal,
    "gaussian": _sample_gaussian,
    "uniform": _sample_uniform,
}

def generate_representative_test_vectors(
    X,
    config: DataConfig
):
    """
    Generate statistically representative test vectors from dataset statistics.

    Parameters
    ----------
    X : np.ndarray
        Client-side feature matrix.
    num_samples : int
        Number of test vectors to generate.
    method : str
        Sampling strategy. One of: 'truncated_normal', 'gaussian', 'uniform'.
    rounding : int or None
        Decimal rounding applied to generated samples.
    random_state : int or None
        RNG seed for reproducibility.

    Returns
    -------
    np.ndarray
        Shape (num_samples, num_features)
    """

    method = config.method
    num_samples = config.num_samples
    rounding = config.rounding
    
    if method not in _SAMPLERS:
        raise ValueError(f"Unknown sampling method '{method}'")

    rng = np.random.default_rng(config.random_state)
    descriptors = _compute_feature_descriptors(X)

    test_vectors = _SAMPLERS[method](descriptors, num_samples, rng)

    if rounding is not None:
        test_vectors = np.round(test_vectors, rounding)

    return test_vectors

