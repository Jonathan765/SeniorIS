import time
import numpy as np

from .metrics import InferenceEvaluationResult
from .inference_evaluator import InferenceEvaluator
from ckks_param_tool.params import CKKSParams
from ckks_param_tool.encryption import TenSEALBackend
from ckks_param_tool.config import EvaluationConfig


class TenSEALInferenceEvaluator(InferenceEvaluator):

    def __init__(self, model, X, config: EvaluationConfig):
        
        self.backend = TenSEALBackend
        self.model = model
        self.X = X
        self.num_samples = config.num_samples

    def evaluate(self, params: CKKSParams) -> InferenceEvaluationResult:
        
        try:
            backend = self.backend(params) 

            idx = np.random.choice(self.X.shape[0], size=self.num_samples, replace=False)
            X_sample = self.X[idx, :]

            errors = []

            start = time.time()

            for sample in X_sample:
                enc_x = backend.encrypt(sample)
                enc_y = self.model(enc_x)
                dec_y = backend.decrypt(enc_y)
                plain_y = np.array(self.model(np.array(sample)))

                err = float(np.mean(np.abs(dec_y - plain_y)))
                errors.append(err)

            runtime = time.time() - start

            return InferenceEvaluationResult(
                error=max(errors),
                runtime=runtime,
            )

        except Exception as e:
            return InferenceEvaluationResult(
                error=np.inf,
                runtime=np.inf,
            )