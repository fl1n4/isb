import logging


logging.basicConfig(level=logging.INFO)


def encoder(input_file:str,
            output_file:str,
            shift:int) -> None:
    """
    a function for encrypting text with monoalphabetic substitution
    :param input_file: The path to the source text file.
    :param output_file: The path to the new text file where the modified text will be saved.
    :param shift: The meaning of the alphabet shift.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        encoder_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    encoder_text += chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
                else:
                    encoder_text += chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
            else:
                encoder_text += char

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(encoder_text)
    except FileNotFoundError as e:
        logging.error(f"File not found: {e.filename}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    input_file = "C:/Users/zhura/Desktop/isb/lab_1/original_text.txt"
    output_file = 'C:/Users/zhura/Desktop/isb/lab_1/crypted.txt'
    shift = 3
    encoder(input_file, output_file, shift)