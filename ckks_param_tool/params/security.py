import numpy as np

ALLOWED_CHAIN_BITS = {
    8192: 218, 
    16384: 438, 
    32768: 881
}

def calculate_security_score(deg, chain_sum):

    # Compute relative score normalized to 128-bit baseline
    base = ALLOWED_CHAIN_BITS[deg]  
    
    relative = base / chain_sum  
    # Weight slightly by degree
    weight = np.log2(deg / 8192 + 1)
    return relative * weight