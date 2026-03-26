import time
import numpy as np

from .metrics import ParameterEvaluationResult
from .parameter_evaluator import ParameterEvaluator
from ckks_param_tool.params import CKKSParams
from ckks_param_tool.encryption import TenSEALBackend
from ckks_param_tool.config import EvaluationConfig

'''
This file contains the parameter evalation class that outlines the process of evaluating
candidate parameters using TenSEAL.
'''

class TenSEALParameterEvaluator(ParameterEvaluator):

    def __init__(self, model, test_vectors):

        self.backend = TenSEALBackend
        self.model = model
        self.test_vectors = test_vectors

    # given a parameter set, return a ParameterEvaluationResult object
    def evaluate(self, params: CKKSParams) -> ParameterEvaluationResult:
        try:

            # initialize TenSEAL backend using parameters
            backend = self.backend(params) 

            errors = []
            runtimes = []
            
            for vec in self.test_vectors:
                start = time.time()

                # encrypted inference
                enc_x = backend.encrypt(vec)
                enc_y = self.model.forward_encrypted(enc_x)
                dec_y = backend.decrypt(enc_y)

                # calculate runtime
                runtime = time.time() - start
                runtimes.append(runtime)

                # calculate error
                plain_y = np.array(self.model(np.array(vec)))
                err = float(np.mean(np.abs(dec_y - plain_y)))

                errors.append(err)

            return ParameterEvaluationResult(
                error=max(errors),
                runtime=np.mean(runtimes),
                security_bits=params.security_score,
                status="success",
                failure_reason=""
            )

        # handle case when encrypted inference fails, stores failure reason
        except Exception as e:
            return ParameterEvaluationResult(
                error=np.inf,
                runtime=np.inf,
                security_bits=0.0,
                status="failure",
                failure_reason=str(e)
            )

