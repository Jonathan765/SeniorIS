import itertools
from ckks_param_tool.params import CKKSParams

ALLOWED_CHAIN_BITS = {
    8192: 218,
    16384: 438,
    32768: 881
}

VALID_CHAIN_PRIME_SIZES = (40, 60)

def _valid_degrees_for_depth(depth: int) -> list[int]:
    degrees = []
    if depth <= 7:
        degrees.append(8192)
    if depth <= 14:
        degrees.append(16384)
    if depth <= 29:
        degrees.append(32768)
    return degrees

def _generate_valid_chains(
    poly_degree: int,
    depth: int
) -> list[tuple[int, ...]]:

    max_bits = ALLOWED_CHAIN_BITS[poly_degree]
    chains = []

    for L in (depth + 1, depth + 2):
        for tail in itertools.product(VALID_CHAIN_PRIME_SIZES, repeat=L - 1):
            chain = (60,) + tail
            if sum(chain) <= max_bits:
                chains.append(chain)

    return chains

class CKKSParameterSearchSpace:
    def __init__(self, depth: int):
        self.depth = depth

    def generate(self) -> list[CKKSParams]:
        params = []

        degrees = _valid_degrees_for_depth(self.depth)
        scales = (2**40, 2**50, 2**60)

        for deg in degrees:
            chains = _generate_valid_chains(deg, self.depth)
            for chain in chains:
                for scale in scales:
                    params.append(
                        CKKSParams(
                            poly_degree=deg,
                            scale=scale,
                            chain=chain
                        )
                    )

        return params
