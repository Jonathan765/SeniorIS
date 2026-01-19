#Datasets:
from data.loaders import load_breast_cancer_data
from data.loaders import load_diabetes_data

#Models:
from data.splits import client_server_split
from models.training import train_linear_regression
from models.training import train_logistic_regression

#Test vectors:
from data.generators import generate_representative_test_vectors

from encryption.tenseal_backend import TenSEALBackend
from tool.evaluation.tenseal_evaluator import TenSEALParameterEvaluator
from tool.evaluation.tenseal_evaluator import TenSEALInferenceEvaluator
from tool.search_space import CKKSParameterSearchSpace
from tool.selection.objective import ErrorObjective
from tool.selection.tenseal_selector import CKKSParameterSelector

from tool.plotting.plotting import plot_precision_vs_security
from tool.plotting.plotting import plot_runtime_vs_precision
from tool.plotting.plotting import plot_runtime_vs_security
from tool.plotting.plotting import results_to_dataframe

from tool.config import load_config
from tool.config import ExperimentConfig

# def run_ckks_tenseal_parameter_search_expirement(X, model, config):

#     config = load_config("config.json")
#     test_vectors = generate_representative_test_vectors(X)

#     evaluator = TenSEALParameterEvaluator(
#         backend=TenSEALBackend,
#         model=model,
#         test_vectors=test_vectors
#     )

#     selector = CKKSParameterSelector(
#         evaluator=evaluator,
#         search_space=CKKSParameterSearchSpace(model.multiplicative_depth),
#         constraints=None,
#         objective=ErrorObjective()
#     )




# def run():
    
#     config = load_config("config.json")

#     X, y = load_diabetes_data()
#     X_client, X_server, y_client, y_server = client_server_split(X, y)

#     test_vectors = generate_representative_test_vectors(X_client)

#     model = train_linear_regression(X_server, y_server)

#     evaluator = TenSEALParameterEvaluator(
#         backend=TenSEALBackend,
#         model=model,
#         test_vectors=test_vectors
#     )

#     selector = CKKSParameterSelector(
#         evaluator=evaluator,
#         search_space=CKKSParameterSearchSpace(model.multiplicative_depth),
#         constraints=None,
#         objective=ErrorObjective()
#     )

#     results = selector.select()
#     print("Best Parameter Set:", results[0])

#     best_params = results[0][0]

#     inference_evaluator = TenSEALInferenceEvaluator(
#         backend=TenSEALBackend,
#         model=model,
#         X=X_client
#     )
#     inference_results = inference_evaluator.evaluate(best_params, 10)

#     print("Inference output:", inference_results)
 
#     df = results_to_dataframe(results)
#     plot_precision_vs_security(df)
#     plot_runtime_vs_precision(df)
#     plot_runtime_vs_security(df)

from experiment import Experiment

if __name__ == "__main__":

    X, y = load_diabetes_data()
    X_client, X_server, y_client, y_server = client_server_split(X, y)

    model = train_linear_regression(X_server, y_server)

    expirement = Experiment(X_client, model, "config.json")

    experiment.run()


