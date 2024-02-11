def encoder(input_file, output_file, shift):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    encoder_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encoder_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encoder_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encoder_text += char

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(encoder_text)


input_file = 'text.txt'
output_file = 'output.txt'
shift = 3


encoder(input_file, output_file, shift)