def replace_letter_in_file(input_text:str, output_text:str, target_letter:str, new_letter:str, indexes):
    """
    Заменяет все вхождения целевой буквы на заменяющую букву в текстовом файле
    и сохраняет результат в новый файл. При наличии индекса в списке индексов, буква остается без изменений.

    :param input_text: Путь к исходному текстовому файлу.
    :param output_text: Путь к новому текстовому файлу, куда будет сохранен измененный текст.
    :param target_letter: Буква, которую нужно заменить.
    :param new_letter: Буква, на которую нужно заменить целевую букву.
    :param indexes: Список индексов замененных букв.
    """
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