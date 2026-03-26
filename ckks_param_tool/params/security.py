import numpy as np

'''
This file contains the tables outlined by the Homomorphic Encryption Standard that ensure
128, 192, and 256 bit security.
'''

ALLOWED_CHAIN_BITS = {
    8192: 218, 
    16384: 438, 
    32768: 881
}

SECURITY_TABLES = {
    128: {
        8192: 218,
        16384: 438,
        32768: 881,
    },
    192: {
        8192: 165,
        16384: 330,
        32768: 660,
    },
    256: {
        8192: 110,
        16384: 220,
        32768: 440,
    },
}

# this function returns the highest security level satisfied by (N, sum(qi)) using the tables
def security_level(poly_degree: int, total_modulus_bits: int) -> int:
    for sec in sorted(SECURITY_TABLES, reverse=True):
        if total_modulus_bits <= SECURITY_TABLES[sec][poly_degree]:
            return sec
    return 0

