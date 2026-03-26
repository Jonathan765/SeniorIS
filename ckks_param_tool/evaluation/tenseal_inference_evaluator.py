import time
import numpy as np

from .metrics import InferenceEvaluationResult
from .inference_evaluator import InferenceEvaluator
from ckks_param_tool.params import CKKSParams
from ckks_param_tool.encryption import TenSEALBackend
from ckks_param_tool.config import EvaluationConfig

'''
This file contains the TenSEAL inference evaluation class, which defines how a given 
recommended parameter set will be evaluated.
'''
class TenSEALInferenceEvaluator(InferenceEvaluator):

    def __init__(self, model, X, config: EvaluationConfig):
        
        self.backend = TenSEALBackend
        self.model = model
        self.X = X
        self.num_samples = config.num_samples
        self.rng = np.random.default_rng(seed=42)

    # Given a parameter set, returns an InferenceEvaluationResult object
    def evaluate(self, params: CKKSParams) -> InferenceEvaluationResult:
        
        try:
            # initializing the backend (TenSEAL)
            backend = self.backend(params) 

            # indices of random dataset entries
            idx = self.rng.choice(self.X.shape[0], size=self.num_samples, replace=False)

            # selecting the random entries
            X_sample = self.X[idx, :]

            errors = []

            runtimes = []
            

            for sample in X_sample:
                
                start = time.time()
                # encrypted inference
                enc_x = backend.encrypt(sample) # encrypt random entry
                enc_y = self.model.forward_encrypted(enc_x) # homomorphic forward pass
                dec_y = backend.decrypt(enc_y) # decrypt

                # calculate runtime
                end = time.time() - start

                # baseline used for metrics, plaintext inference
                plain_y = np.array(self.model(np.array(sample))) 
                
                # calculate error
                err = float(np.mean(np.abs(dec_y - plain_y)))

                errors.append(err)
                runtimes.append(end) 


            return InferenceEvaluationResult(
                error=max(errors), # record maximum error accross dataset samples
                runtime=np.mean(runtimes), # record average runtime across dataset samples
            )

        # handle case of encrypted inference fails
        except Exception as e:
            return InferenceEvaluationResult(
                error=np.inf,
                runtime=np.inf,
            )