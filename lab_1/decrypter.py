import logging
from typing import List


logging.basicConfig(level=logging.INFO)


def replace_letter_in_file(input_text:str, 
                           output_text:str, 
                           target_letter:str, 
                           new_letter:str, 
                           indexes: List[int]) -> None:
    """
    Replaces all occurrences of the target letter with the replacement letter in the text file
    and saves the result to a new file. If there is an index in the index list, the letter remains unchanged.

    :param input_text: The path to the source text file.
    :param output_text: The path to the new text file where the modified text will be saved.
    :param target_letter: The letter that needs to be replaced.
    :param new_letter: The letter to replace the target letter with.
    :param indexes: A list of the indexes of the replaced letters.
    """
    try:
        with open(input_text, 'r', encoding='utf-8') as file:
            default_text = file.read()

        new_text = ""

        for index, letter in enumerate(default_text):
            if index in indexes:
                new_text += letter
            elif letter == target_letter:
                new_text += new_letter
                indexes.append(index)
            else:
                new_text += letter

        with open(output_text, 'w', encoding='utf-8') as new_file:
            new_file.write(new_text)
    except FileNotFoundError as e:
        logging.error(f"File not found: {e.filename}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    path_to_input = 'C:/Users/zhura/Desktop/isb/lab_1/cod5.txt'
    path_to_output = 'C:/Users/zhura/Desktop/isb/lab_1/decrypted_text.txt'
    indexes_new_letters = []
    replace_letter_in_file(path_to_input, path_to_output, 'Е', 'О', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'М', ' ', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'И', 'С', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, '7', 'Ж', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, '2', 'М', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, '>', 'Е', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, '<', 'Ч', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'У', 'И', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, '4', 'А', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, ' ', 'Ы', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'Д', 'Н', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'Р', 'Д', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'П', 'Г', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'Ч', 'У', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'Й', 'Т', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'Х', 'К', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, '8', 'З', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'О', 'В', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'А', 'Ь', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, '1', 'Л', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 't', 'Р', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'r', 'П', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'Л', 'Я', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'Ъ', 'Ц', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'Щ', 'Х', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'К', 'Ю', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'Ш', 'Ф', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, '5', 'Б', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'Ф', 'Й', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'Ы', 'Ш', indexes_new_letters)
    replace_letter_in_file(path_to_output, path_to_output, 'Ь', 'Щ', indexes_new_letters)