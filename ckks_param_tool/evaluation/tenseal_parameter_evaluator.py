import time
import numpy as np

from .metrics import ParameterEvaluationResult
from .parameter_evaluator import ParameterEvaluator
from ckks_param_tool.params import CKKSParams
from ckks_param_tool.encryption import TenSEALBackend
from ckks_param_tool.config import EvaluationConfig


class TenSEALParameterEvaluator(ParameterEvaluator):
    """
    Evaluates CKKS parameters using an encryption backend.
    """

    def __init__(self, model, test_vectors):
        """
        backend: EncryptionBackend (TenSEALBackend)
        model: callable model
        test_vectors: list[np.ndarray]
        """
        self.backend = TenSEALBackend
        self.model = model
        self.test_vectors = test_vectors

    def evaluate(self, params: CKKSParams) -> ParameterEvaluationResult:
        try:

            backend = self.backend(params) 

            errors = []
            start = time.time()

            for vec in self.test_vectors:
                enc_x = backend.encrypt(vec)
                enc_y = self.model(enc_x)

                dec_y = backend.decrypt(enc_y)
                plain_y = np.array(self.model(np.array(vec)))

                err = float(np.mean(np.abs(dec_y - plain_y)))
                errors.append(err)

            runtime = time.time() - start

            return ParameterEvaluationResult(
                error=max(errors),
                runtime=runtime,
                security_bits=params.security_score
            )

        except Exception as e:
            return ParameterEvaluationResult(
                error=np.inf,
                runtime=np.inf,
                security_bits=0.0
            )

