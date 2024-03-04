import json
import logging


logging.basicConfig(level=logging.INFO)


def encoder(input_file: str, output_file: str, shift: int) -> None:
    """
    Encrypts text with monoalphabetic substitution and saves the modified text to a new file.
    
    :param input_file: The path to the source text file.
    :param output_file: The path to the new text file where the modified text will be saved.
    :param shift: The meaning of the alphabet shift.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        encoder_text = ""
        encoding_dict = {}

        for char in text:
            if char.isalpha():
                base_char = 'a' if char.islower() else 'А'
                encoded_char = chr((ord(char) - ord(base_char) + shift) % 32 + ord(base_char))
                encoder_text += encoded_char
                encoding_dict[char] = encoded_char
            else:
                encoder_text += char

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(encoder_text)

        with open('key1.json', 'w', encoding='utf-8') as json_file:
            json.dump(encoding_dict, json_file, ensure_ascii=False)

    except FileNotFoundError as e:
        logging.error(f"File not found: {e.filename}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    input_file = "C:/Users/zhura/Desktop/isb/lab_1/original_text.txt"
    output_file = 'C:/Users/zhura/Desktop/isb/lab_1/crypted.txt'
    shift = 3
    encoder(input_file, output_file, shift)