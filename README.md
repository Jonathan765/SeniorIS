# CKKS Parameter Recommendation Tool

This project presents an automated, data-driven tool for selecting parameters in the CKKS homomorphic encryption scheme for privacy-preserving machine learning.

The tool analyzes both dataset characteristics and model behavior to generate and evaluate candidate parameter configurations, providing users with a trade-off analysis between runtime, precision, and security.

---

## Overview

Homomorphic encryption enables secure outsourced computation, but its practical adoption is limited by complex parameter selection. This project addresses this challenge of usability by:
- Automatically generating a search space of parameter configurations that reflect the underlying dataset and machine learning model.
- Evaluating candidate configurations using representative test vectors that preserve privacy.
- Identifying Pareto-optimal trade-offs between runtime and precision among candidates at each securit level.
- Recommend an optimal parameter set and evaluating it under real dataset inference.

---

## Project Structure

The project is organized into modular components corresponding to each stage of the CKKS parameter selection tool pipeline:

```text

ckks_param_tool/
├── config/ # Configuration objects for experiment settings
├── data/ # Dataset handling and preprocessing utilities
├── encryption/ # TenSEAL CKKS encryption backend
├── evaluation/ # Candidate parameter and recommended parameter evaluation 
├── experiment/ # Main experiment management
├── models/ # Machine learning model definitions
├── params/ # CKKS parameter representation and metric definitions
├── plotting/ # Visualization utilities
├── search/ # Parameter search space construction and Pareto selection
└── init.py

```

