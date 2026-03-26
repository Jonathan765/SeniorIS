'''
This file contains the memory estimation function for a given parameter set
'''

BYTES_PER_COEFF = 8 # hardware specific, default choice for 64-bit systems

def _rns_poly_bytes(poly_degree: int, chain_sum: int) -> int:
    return poly_degree * chain_sum * BYTES_PER_COEFF

def _poly_bytes_for_chain(N, chain):
        return sum(_rns_poly_bytes(N, qi) for qi in chain)

# given (N,Q), returns the estimated memory footprint.
def estimate_ckks_memory(
    poly_degree: int,
    chain: tuple[int, ...],
) -> dict[str, int]:
    N = poly_degree
    
    poly = _poly_bytes_for_chain(N, chain)

    return {
        "secret_key": poly,
        "public_key": 2 * poly,
        "relin_keys": 2 * poly * len(chain),
        "ciphertext": 2 * poly,
        "context": poly,
        "total": (
            poly +
            2 * poly +
            2 * poly * len(chain) +
            2 * poly +
            poly
        )
    }