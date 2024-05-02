import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import (Cipher, 
                                                    algorithms, 
                                                    modes)

class SymmCrypt:

    def __init__(self, key_len: int) -> None:
        self.key_len = key_len

    def generate_key(self) -> bytes:
        return os.urandom(self.key_len//8)
    
    def encrypt_text(self, sym_key:bytes, encrypted_text_path: bytes, text: bytes) -> None:
        iv = os.urandom(8)
        cipher = Cipher(algorithms.CAST5(sym_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_text = padder.update(text) + padder.finalize()
        ciphertext = iv + encryptor.update(padded_text) + encryptor.finalize()

        with open(encrypted_text_path, "wb") as encrypted_text_file:
            encrypted_text_file.write(ciphertext)
    
    def decrypt_text(self, sym_key: bytes, decrypted_text_path: str) -> None:
        iv = ciphertext[:8]
        ciphertext = ciphertext[8:]
        cipher = Cipher(algorithms.CAST5(sym_key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(plaintext) + unpadder.finalize()

        with open(decrypted_text_path, "wb") as decrypted_text_file:
            decrypted_text_file.write(plaintext)