import os
import json
import logging


logging.basicConfig(level=logging.INFO)


def get_encoder_paths(params):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_directory, params.get('input_file'))
    output_file = os.path.join(current_directory, params.get('output_file'))
    shift = params.get('shift')
    key_file = os.path.join(current_directory, params.get('key'))
    return {'input_file': input_file, 'output_file': output_file, 'shift': shift, 'key_file': key_file}

def encoder(json_file_path: str) -> None:
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            params = json.load(json_file)

        paths = get_encoder_paths(params)

        with open(paths['input_file'], 'r', encoding='utf-8') as file:
            text = file.read()

        encoder_text = ""
        encoding_dict = {}

        for char in text:
            if char.isalpha():
                base_char = 'а' if char.islower() else 'А'
                encoded_char = chr((ord(char) - ord(base_char) + paths['shift']) % 32 + ord(base_char))
                encoder_text += encoded_char
                encoding_dict[char] = encoded_char
            else:
                encoder_text += char

        with open(paths['output_file'], 'w', encoding='utf-8') as file:
            file.write(encoder_text)

        with open(paths['key_file'], 'w', encoding='utf-8') as json_file:
            json.dump(encoding_dict, json_file, ensure_ascii=False)

    except FileNotFoundError as e:
        logging.error(f"File not found: {e.filename}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    json_file_path = 'part1/params1.json'
    encoder(json_file_path)