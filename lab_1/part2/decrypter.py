import logging
from typing import List


logging.basicConfig(level=logging.INFO)


def replace_keys_with_values(json_file: str, input_file: str, output_file: str) -> None:
    """
    Replace keys in the input text file with their corresponding values from the JSON file
    and write the modified text to the output file.
    
    json_file (str): Path to the JSON file containing key-value pairs.
    input_file (str): Path to the input text file.
    output_file (str): Path to the output text file.
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except Exception as e:
        logging.error(f"An error occurred while reading the JSON file: {e}")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            original_text = f.read()
    except Exception as e:
        logging.error(f"An error occurred while reading the input file: {e}")
        return

    for key, value in json_data.items():
        original_text = original_text.replace(key, value)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(original_text)
        logging.info(
            "Replacement completed successfully. Results written to the output file.")
    except Exception as e:
        logging.error(
            f"An error occurred while writing to the output file: {e}")


if __name__ == '__main__':
    path_to_input = 'C:/Users/zhura/Desktop/isb/lab_1/part1/cod1.txt'
    path_to_output = 'C:/Users/zhura/Desktop/isb/lab_1/part1/decrypted_text1.txt'
    indexes_new_letters = []