import os
import json
import logging


logging.basicConfig(level=logging.INFO)


def get_file_paths(params):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_directory, params.get('input_file'))
    output_file = os.path.join(current_directory, params.get('output_file'))
    key_file_path = os.path.join(current_directory, params.get('key'))
    return {'input_file': input_file, 'output_file': output_file, 'key_file_path': key_file_path}

def replace_letters(params):
    try:
        with open(params, 'r', encoding='utf-8') as json_file:
            params = json.load(json_file)
        paths = get_file_paths(params)

    except FileNotFoundError as e:
        logging.error(f"File not found: {e.filename}")
        return
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        return
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return

    try:
        with open(paths['input_file'], 'r', encoding='utf-8') as file:
            text = file.read()
        
        with open(paths['key_file_path'], 'r', encoding='utf-8') as key_file:
            key_mapping = json.load(key_file)

        for key, value in key_mapping.items():
            text = text.replace(value, key)

        with open(paths['output_file'], 'w', encoding='utf-8') as file:
            file.write(text)

    except FileNotFoundError as e:
        logging.error(f"File not found: {e.filename}")
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON in key file: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during file processing: {e}")


if __name__ == '__main__':
    json_file_path = 'part2/params2.json'
    replace_letters(json_file_path)