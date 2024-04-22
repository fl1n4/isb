import os

from cryptography.hazmat.primitives import (hashes,
                                            padding,
                                            serialization)
from cryptography.hazmat.primitives.ciphers import (Cipher, 
                                                    algorithms, 
                                                    modes)


class HybridEncryptor:
    def __init__(self, text_file_path, private_key_path, encrypted_sym_key_path, encrypted_text_path):
        self.text_file_path = text_file_path
        self.private_key_path = private_key_path
        self.encrypted_sym_key_path = encrypted_sym_key_path
        self.encrypted_text_path = encrypted_text_path
    
    def encrypt_data(self):
        with open(self.text_file_path, "rb") as text_file:
            plaintext = text_file.read()

        with open(self.private_key_path, "rb") as private_key_file:
            private_key = serialization.load_pem_private_key(
                private_key_file.read(),
                password=None
            )
        
        with open(self.encrypted_sym_key_path, "rb") as encrypted_sym_key_file:
            encrypted_sym_key = encrypted_sym_key_file.read()
        
        sym_key = private_key.decrypt(
            encrypted_sym_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        iv = os.urandom(16)
        cipher = Cipher(algorithms.CAST5(sym_key), modes.CFB(iv))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()

        with open(self.encrypted_text_path, "wb") as encrypted_text_file:
            encrypted_text_file.write(ciphertext)