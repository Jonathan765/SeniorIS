#Config
from ckks_param_tool.config import (
    load_experiment_config,
    ExperimentConfig
)

#Test vectors:
from ckks_param_tool.data import generate_representative_test_vectors

#Evaluation:
from ckks_param_tool.evaluation import (
    TenSEALParameterEvaluator,
    TenSEALInferenceEvaluator
)

#Search:
from ckks_param_tool.search import (
    CKKSParameterSearchSpace,
    ErrorObjective,
    CKKSParameterSelector
)

#Plotting:
from ckks_param_tool.plotting import (
    results_to_dataframe,
    plot_precision_vs_security,
    plot_runtime_vs_precision,
    plot_runtime_vs_security
)
import matplotlib.pyplot as plt

#Return object:
from .metrics import ExperimentResult

#Saving:
from pathlib import Path
from datetime import datetime
import json

class Experiment:
    def __init__(self, dataset, model, config):
        self.dataset = dataset
        self.model = model
        self.config = load_experiment_config(config)
        self.results = None
    
    def run(self) -> ExperimentResult:

        test_vectors = generate_representative_test_vectors(
            self.dataset, 
            self.config.data
        )

        evaluator = TenSEALParameterEvaluator(
            model=self.model,
            test_vectors=test_vectors
        )

        selector = CKKSParameterSelector(
            evaluator=evaluator,
            search_space=CKKSParameterSearchSpace(self.model.multiplicative_depth),
            config=self.config.selection
        )

        param_search_results = selector.select()
        best_params, best_eval, best_score = param_search_results[0]
        
        inference_evaluator = TenSEALInferenceEvaluator(
            model=self.model,
            X=self.dataset,
            config=self.config.evaluation
        )
        inference_result = inference_evaluator.evaluate(best_params)

        self.results = ExperimentResult(
            param_search_results=param_search_results,
            best_params=best_params,
            inference_result=inference_result
        )

        return self.results

    def plot(self, output_dir=None, show=True):
        if self.results is None:
            raise RuntimeError("Experiment not run.")

        df = results_to_dataframe(self.results.param_search_results)

        figs = {
            "precision_vs_security": plot_precision_vs_security(df, self.config.plotting),
            "runtime_vs_precision": plot_runtime_vs_precision(df, self.config.plotting),
            "runtime_vs_security": plot_runtime_vs_security(df, self.config.plotting)
        }

        if output_dir:
            output_dir = Path(output_dir)
            output_dir.mkdir(exist_ok=True)
            for name, fig in figs.items():
                fig.savefig(output_dir / f"{name}.png")
                plt.close(fig)

        if show:
            for fig in figs.values():
                fig.show()

        return figs


    def _save_config(self, run_dir: Path):
        with open(run_dir / "config.json", "w") as f:
            json.dump(self.config.to_dict(), f, indent=2)

    def _save_param_search(self, run_dir: Path):
        df = results_to_dataframe(
            self.results.param_search_results
        )
        df.to_csv(run_dir / "param_search.csv", index=False)

    def _save_inference(self, run_dir: Path):
        with open(run_dir / "inference.json", "w") as f:
            json.dump(
                self.results.inference_result.to_dict(),
                f,
                indent=2
            )
    
    def _save_plots(self, run_dir: Path):
        plots_dir = run_dir / "plots"
        plots_dir.mkdir()
        self.plot(output_dir=plots_dir, show=False)


    def save(self, output_dir: str | Path):

        if self.results is None:
            raise RuntimeError("Cannot save before running experiment.")

        output_dir = Path(output_dir)

        run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        run_dir = output_dir / run_id
        run_dir.mkdir(parents=True, exist_ok=False)

        self._save_config(run_dir)

        self._save_param_search(run_dir)

        self._save_inference(run_dir)

        self._save_plots(run_dir)

        return run_dir

    
    