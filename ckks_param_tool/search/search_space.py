import itertools
from ckks_param_tool.params import CKKSParams
from .policy import CKKSSearchPolicy
import math

'''
This file contains the class that defines the search space generation functionality
'''
class CKKSParameterSearchSpace:
    def __init__(self, depth: int, bits_integer: int, bits_decimal: int, policy=None):
        self.depth = depth
        self.bits_integer = bits_integer
        self.bits_decimal = bits_decimal
        self.policy = policy or CKKSSearchPolicy.default()

    # generates the candidate parameter search space according to the policy
    def generate(self) -> list[CKKSParams]:
        params = []

        degrees = self.policy.valid_degrees(self.depth)
        scales = self.policy.candidate_scales(self.bits_decimal, self.depth)

        for deg in degrees:
            for scale in scales:
                chains = self.policy.generate_chains(
                    poly_degree=deg,
                    scale_bits=scale,
                    depth=self.depth,
                    bits_integer=self.bits_integer,
                    bits_decimal=self.bits_decimal,
                )
                for chain in chains:
                    params.append(
                        CKKSParams(
                            poly_degree=deg,
                            scale=2**scale,
                            chain=chain
                        )
                    )

        return params

