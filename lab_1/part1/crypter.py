import json
import logging


logging.basicConfig(level=logging.INFO)


def encoder(json_file_path: str) -> None:
    """
    Encrypts text with monoalphabetic substitution and saves the modified text to a new file.
    
    :param input_file: The path to the source text file.
    :param output_file: The path to the new text file where the modified text will be saved.
    :param shift: The meaning of the alphabet shift.
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            params = json.load(json_file)

        input_file = params.get('input_file')
        output_file = params.get('output_file')
        shift = params.get('shift')
        key_file = params.get('key')

        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        encoder_text = ""
        encoding_dict = {}

        for char in text:
            if char.isalpha():
                base_char = 'а' if char.islower() else 'А'
                encoded_char = chr((ord(char) - ord(base_char) + shift) % 32 + ord(base_char))
                encoder_text += encoded_char
                encoding_dict[char] = encoded_char
            else:
                encoder_text += char

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(encoder_text)

        with open(key_file, 'w', encoding='utf-8') as json_file:
            json.dump(encoding_dict, json_file, ensure_ascii=False)

    except FileNotFoundError as e:
        logging.error(f"File not found: {e.filename}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    json_file_path = 'C:/Users/zhura/Desktop/isb/lab_1/part1/params1.json'
    encoder(json_file_path)