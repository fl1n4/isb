import os
import json
from math import sqrt, pow
from scipy.special import erfc
import mpmath


pi = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}


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
        return 0
    else:
        V = sum(int(bitstring[i] != bitstring[i+1]) for i in range(N-1))
        p_value = erfc(abs(V-2*N*E*(1-E))/(2*sqrt(2*N)*E*(1-E)))
        return p_value
    

def longest_run_of_ones_test(bitstring):
    N = len(bitstring)
    block_size=8
    M = block_size

    max_run_lengths = [max(len(run) for run in block.split('0')) for block in [bitstring[i:i+M] for i in range(0, N, M)]]

    v1 = sum(1 for length in max_run_lengths if length <= 1)
    v2 = sum(1 for length in max_run_lengths if length == 2)
    v3 = sum(1 for length in max_run_lengths if length == 3)
    v4 = sum(1 for length in max_run_lengths if length >= 4)
    V = [v1, v2, v3, v4]

    x_square = 0
    for i in range(4):
        x_square += pow(V[i] - 16 * pi[i], 2) / (16 * pi[i])
    p_value = mpmath.gammainc(3/2, x_square/2)

    return p_value


if __name__ == "__main__":
    with open(os.path.join("lab_2", "task1", "results_of_generators.json"), "r") as sequences:
        sequence = json.load(sequences)

    cpp_sequence = sequence['cpp']
    java_sequence = sequence['java']

    with open(os.path.join("lab_2", "task2", "result_of_tests.txt"), 'w') as sequences:
        sequences.write("Results(C++)\n")
        sequences.write(str(frequency_test(cpp_sequence)) + '\n')
        sequences.write(str(runs_test(cpp_sequence)) + '\n')
        sequences.write(str(longest_run_of_ones_test(cpp_sequence)) + '\n')

        sequences.write("\nResults(Java)\n")
        sequences.write(str(frequency_test(java_sequence)) + '\n')
        sequences.write(str(runs_test(java_sequence)) + '\n')
        sequences.write(str(longest_run_of_ones_test(java_sequence)) + '\n')