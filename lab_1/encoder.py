def encoder(input_file, output_file, shift):
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


input_file = "C:/Users/zhura/Desktop/isb/lab_1/original_text.txt"
output_file = 'output.txt'
shift = 3


encoder(input_file, output_file, shift)