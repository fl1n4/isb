import os
import argparse

from AsymmCrypt import AsymmCrypt
from SymmCrypt import SymmCrypt
from HelpFunc import HelpFunc


def main():
    parser = argparse.ArgumentParser(description="Single entry point for key generation, encryption, and decryption.")
    parser.add_argument('mode', choices=['gen', 'enc', 'dec'], help='Mode of operation')

    parser.add_argument('-k', '--key_length', type=int, default=128, help='Length of the symmetric key in bits (default: 128).')
    parser.add_argument('-t', '--text_file', type=str, default=os.path.join('lab_3','texts','text.txt'), help='Path to the text file (default: lab_3/texts/text.txt).')
    parser.add_argument('-pk', '--public_key', type=str, default=os.path.join('lab_3','keys','public_key.pem'), help='Path to the public key file (default: lab_3/keys/public_key.pem).')
    parser.add_argument('-sk', '--private_key', type=str, default=os.path.join('lab_3','keys','private_key.pem'), help='Path to the private key file (default: lab_3/keys/private_key.pem).')
    parser.add_argument('-skf', '--symmetric_key_file', type=str, default=os.path.join('lab_3','keys','sym_key.txt'), help='Path to the symmetric key file (default: lab_3/keys/sym_key.txt).')
    parser.add_argument('-et', '--encrypted_text_file', type=str, default=os.path.join('lab_3','texts','encrypted_text.txt'), help='Path to the encrypted text file (default: lab_3/texts/encrypted_text.txt).')
    parser.add_argument('-dt', '--decrypted_text_file', type=str, default=os.path.join('lab_3','texts','decrypted_text.txt'), help='Path to the decrypted text file (default: lab_3/texts/decrypted_text.txt).')
    parser.add_argument('-ip','--iv_path_file', type=str, default=os.path.join('lab_3','iv_path_file.txt'), help='Path to the iv text file (default: lab_3/iv_path_file.txt)')
    parser.add_argument('-bs', '--block_size', type=int, default=8, help='Block size for iv formation')

    args = parser.parse_args()

    asymm_crypt = AsymmCrypt()
    symm_crypt = SymmCrypt(key_len=args.key_length)
    help_func = HelpFunc()

    match args.mode:
        case 'gen':
            sym_key = symm_crypt.generate_key()
            private_key, public_key = asymm_crypt.generate_key_pair()
            encrypted_sym_key = asymm_crypt.encrypt_with_public_key(public_key, sym_key)
            help_func.write_to_file(args.symmetric_key_file, encrypted_sym_key)
            help_func.serialization_private_key(private_key, args.private_key)
            help_func.serialization_public_key(public_key, args.public_key)

        case 'enc':
            private_key = help_func.deserialization_private_key(args.private_key)
            encrypted_sym_key = help_func.read_file(args.symmetric_key_file)
            decrypted_sym_key = asymm_crypt.decrypt_with_private_key(private_key, encrypted_sym_key)
            text = help_func.read_file(args.text_file)
            symm_crypt.encrypt_text(decrypted_sym_key, args.encrypted_text_file, args.iv_path_file, args.block_size, text)

        case 'dec':
            private_key = help_func.deserialization_private_key(args.private_key)
            encrypted_sym_key = help_func.read_file(args.symmetric_key_file)
            decrypted_sym_key = asymm_crypt.decrypt_with_private_key(private_key, encrypted_sym_key)
            symm_crypt.decrypt_text(decrypted_sym_key, args.decrypted_text_file, args.iv_path_file, args.encrypted_text_file)


if __name__ == "__main__":
    main()