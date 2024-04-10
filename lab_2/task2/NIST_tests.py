import json
import logging
import os
import mpmath
from math import erfc, fabs, pow, sqrt



logging.basicConfig(level=logging.INFO)


pi = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}


def frequency_test(bitstring:str) -> float:
    """
    Performs the frequency (monobit) test for the given bit sequence.

    Parameters:
    bitstring (str): The bit sequence to be tested.

    Returns:
    float: The p-value indicating the degree of agreement of the sequence with a uniform distribution.
    """
    try:
        N = len(bitstring)
        sum_values = fabs(sum(1 if bit == '1' else -1 for bit in bitstring))
        p_value = erfc((sum_values) / sqrt(2*N))
        return p_value
    except Exception as ex:
        logging.error(f"Error occurred during the test execution: {ex}\n")


def runs_test(bitstring:str) -> float:
    """
    Performs the runs test for the given bit sequence.

    Parameters:
    bitstring (str): The bit sequence to be tested.

    Returns:
    float: The p-value indicating the degree of randomness in the sequence of runs.
    """
    try:
        N = len(bitstring)
        ones = bitstring.count('1')
        E = ones / N
        if abs(E - 0.5) >= 2 / sqrt(N):
            return 0
        else:
            V = sum(int(bitstring[i] != bitstring[i+1]) for i in range(N-1))
            p_value = erfc(abs(V-2*N*E*(1-E))/(2*sqrt(2*N)*E*(1-E)))
            return p_value
    except Exception as ex:
            logging.error(f"Error occurred during the test execution: {ex.message}\n{ex.args}\n")
    

def longest_run_of_ones_test(bitstring:str) -> float:
    """
    Performs the longest run of ones test for the given bit sequence.

    Parameters:
    bitstring (str): The bit sequence to be tested.

    Returns:
    float: The p-value indicating the degree of randomness in the distribution of longest runs of ones.
    """
    try:
        N = len(bitstring)
        M = 8 #block size

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
    except Exception as ex:
            logging.error(f"Error occurred during the test execution: {ex.message}\n{ex.args}\n")


if __name__ == "__main__":
    try:
        with open(os.path.join("lab_2","task1","params.json"), "r") as paths:
            path = json.load(paths)
        path1 = path['path_input']
        path2 = path['path_output']

        with open(path1 , "r") as sequences:
            sequence = json.load(sequences)

        cpp_sequence = sequence['cpp']
        java_sequence = sequence['java']

        with open(path2, 'w') as sequences:
            sequences.write("Results(C++)\n")
            sequences.write(str(frequency_test(cpp_sequence)) + '\n')
            sequences.write(str(runs_test(cpp_sequence)) + '\n')
            sequences.write(str(longest_run_of_ones_test(cpp_sequence)) + '\n')

            sequences.write("\nResults(Java)\n")
            sequences.write(str(frequency_test(java_sequence)) + '\n')
            sequences.write(str(runs_test(java_sequence)) + '\n')
            sequences.write(str(longest_run_of_ones_test(java_sequence)) + '\n')
    except FileNotFoundError:
        logging.error("File not found.")
    except json.JSONDecodeError:
        logging.error("Error decoding JSON.")
    except KeyError as e:
        logging.error(f"KeyError: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")