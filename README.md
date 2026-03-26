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

## Installation

### 1. Clone the repository

```bash

git clone https://github.com/your-username/ckks-param-tool.git
cd ckks-param-tool

```

### 2.  Creat a virtual environment

```bash

python3 -m venv venv
source venv/bin/activate 

```

### 3. Install dependencies

```bash

pip install -r requirements.txt

```

## Example Usage

The following example demonstrates how to run the CKKS parameter recommendation tool. The results will be printed to the terminal as well as written to the `results/` directory.

```python

from ckks_param_tool import Experiment
from ckks_param_tool import client_server_split
from ckks_param_tool import load_diabetes_data
from ckks_param_tool import train_linear_regression_model

from pathlib import Path
import os

# Load dataset
X, y = load_diabetes_data()

# Simulate client/server split
X_client, X_server, y_client, y_server = client_server_split(X, y)

# Train model on server-side data
model = train_linear_regression_model(X_server, y_server)

# Initialize experiment
experiment = Experiment(X_client, model)

# Run parameter selection and evaluation
experiment.run(verbose=True)

# Save results
results_dir = Path("results")
experiment.save(results_dir)

```