import tenseal as ts
import numpy as np
from ckks_param_tool.encryption import CKKSBackend
from ckks_param_tool.params import CKKSParams

class TenSEALBackend(CKKSBackend):
    def __init__(self, params: CKKSParams):
        self.params = params
        self.context = self._create_context()

    def _create_context(self):
        ctx = ts.context(
            ts.SCHEME_TYPE.CKKS,
            poly_modulus_degree=self.params.poly_degree,
            coeff_mod_bit_sizes=self.params.chain
        )
        ctx.global_scale = self.params.scale
        ctx.generate_galois_keys()
        return ctx

    def encrypt(self, vector):
        return ts.ckks_vector(self.context, vector)

    def decrypt(self, enc_vector):
        return np.array(enc_vector.decrypt())
