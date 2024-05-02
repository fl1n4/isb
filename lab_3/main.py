import argparse

from AsymmCrypt import AsymmCrypt
from SymmCrypt import SymmCrypt
from HelpFunc import HelpFunc

def main():
    parser = argparse.ArgumentParser(description="Single entry point for key generation, encryption, and decryption.")
    parser.add_argument('mode', choices=['gen', 'enc', 'dec'], help='Mode of operation')

    parser.add_argument('-k', '--key_length', type=int, default=256, help='Length of the symmetric key in bits (default: 256).')
    parser.add_argument('-t', '--text_file', type=str, default='text.txt', help='Path to the text file (default: text.txt).')
    parser.add_argument('-pk', '--public_key', type=str, default='public_key.pem', help='Path to the public key file (default: public_key.pem).')
    parser.add_argument('-sk', '--private_key', type=str, default='private_key.pem', help='Path to the private key file (default: private_key.pem).')
    parser.add_argument('-skf', '--symmetric_key_file', type=str, default='sym_key.bin', help='Path to the symmetric key file (default: sym_key.bin).')
    parser.add_argument('-et', '--encrypted_text_file', type=str, default='encrypted_text.txt', help='Path to the encrypted text file (default: encrypted_text.txt).')
    parser.add_argument('-dt', '--decrypted_text_file', type=str, default='decrypted_text.txt', help='Path to the decrypted text file (default: decrypted_text.txt).')

    args = parser.parse_args()

    asymm_crypt = AsymmCrypt()
    symm_crypt = SymmCrypt(key_len=args.key_length)
    help_func = HelpFunc()

    match args.mode:
        case 'gen':
            private_key, public_key = asymm_crypt.generate_key_pair()
            help_func.serialization_private_key(private_key, args.private_key)
            help_func.serialization_public_key(public_key, args.public_key)

        case 'enc':
            _, public_key = asymm_crypt.generate_key_pair()
            sym_key = symm_crypt.generate_key()
            encrypted_sym_key = asymm_crypt.encrypt_with_public_key(public_key, sym_key)
            help_func.write_to_file(args.symmetric_key_file, encrypted_sym_key)
            symm_crypt.encrypt_text(sym_key, args.encrypted_text_file, args.text_file)

        case 'dec':
            sym_key = help_func.read_from_file(args.symmetric_key_file)
            symm_crypt.decrypt_text(sym_key, args.encrypted_text_file)

if __name__ == "__main__":
    main()