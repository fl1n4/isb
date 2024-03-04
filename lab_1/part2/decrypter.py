import json
import logging


logging.basicConfig(level=logging.INFO)


def replace_letters(json_file_path: str) -> None:
    """
    Replaces all characters in the text by the specified key and saves to a new file.
    
    :param input_file: The path to the source text file.
    :param output_file: The path to the new text file where the modified text will be saved.
    :param key: 
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            params = json.load(json_file)
        input_file = params.get('input_file')
        output_file = params.get('output_file')
        key_file = params.get('key')
    except Exception as e:
        logging.error(f"Error reading the JSON file: {e}")

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
        
    with open(key_file, 'r', encoding='utf-8') as key_file:
        key_mapping = json.load(key_file)

    for key, value in key_mapping.items():
        text = text.replace(value, key)

    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        logging.error(
            f"An error occurred while writing to the output file: {e}")


if __name__ == '__main__':
    json_file_path = 'C:/Users/zhura/Desktop/isb/lab_1/part2/params2.json'
    replace_letters(json_file_path)