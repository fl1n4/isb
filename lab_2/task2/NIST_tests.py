from math import sqrt
from scipy.special import erfc




def frequency_test(bitstring):
    N = len(bitstring)
    sum_values = sum(1 if bit == '1' else -1 for bit in bitstring)
    p_value = erfc((sum_values) / sqrt(2*N))
    return p_value 


def runs_test(bitstring):
    N = len(bitstring)
    ones = bitstring.count('1')
    E = ones / N
    if abs(E - 0.5) >= 2 / sqrt(N):
        return 0  # P-значение равно нулю, если условие не выполнено
    else:
        V = sum(int(bitstring[i] != bitstring[i+1]) for i in range(N-1))
        p_value = erfc(abs(V-2*N*E*(1-E))/(2*sqrt(2*N)*E*(1-E)))
        return p_value