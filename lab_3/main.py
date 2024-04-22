import argparse
import json

from generate_keys import HybridKeyGenerator
from encrypt_data import HybridEncryptor
from decrypt_data import HybridDecryptor

def load_paths_from_json(json_file):
    with open(json_file, "r") as file:
        paths = json.load(file)
    return paths

def main():
    parser = argparse.ArgumentParser(description="Гибридная криптосистема для шифрования данных")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', action='store_true', help='Запускает режим генерации ключей')
    group.add_argument('-enc', '--encryption', action='store_true', help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption', action='store_true', help='Запускает режим дешифрования')

    parser.add_argument('--config', type=str, default='config.json', help='Путь к файлу конфигурации JSON (по умолчанию: config.json)')

    args = parser.parse_args()

    config_file = args.config
    paths = load_paths_from_json(config_file)

    if args.generation:
        generate_keys(paths)
    elif args.encryption:
        encrypt_data(paths)
    else:
        decrypt_data(paths)

def generate_keys(paths):
    key_generator = HybridKeyGenerator(paths["sym_key_path"], paths["public_key_path"], paths["private_key_path"])
    key_generator.generate_keys()

def encrypt_data(paths):
    encryptor = HybridEncryptor(paths["text_file_path"], paths["private_key_path"], paths["encrypted_sym_key_path"], paths["encrypted_text_path"])
    encryptor.encrypt_data()

def decrypt_data(paths):
    decryptor = HybridDecryptor(paths["encrypted_text_path"], paths["private_key_path"], paths["encrypted_sym_key_path"], paths["decrypted_text_path"])
    decryptor.decrypt_data()

if __name__ == "__main__":
    main()