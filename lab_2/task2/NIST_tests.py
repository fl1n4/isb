from math import sqrt
from scipy.special import erfc




def frequency_test(bitstring):
    N = len(bitstring)
    sum_values = sum(1 if bit == '1' else -1 for bit in bitstring)
    p_value = erfc((sum_values) / sqrt(2*N))
    return p_value 