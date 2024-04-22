from cryptography.hazmat.primitives import (hashes,
                                            padding,
                                            serialization)
from cryptography.hazmat.primitives.ciphers import (Cipher, 
                                                    algorithms, 
                                                    modes)


class HybridDecryptor:
    def __init__(self, encrypted_text_path, private_key_path, encrypted_sym_key_path, decrypted_text_path):
        self.encrypted_text_path = encrypted_text_path
        self.private_key_path = private_key_path
        self.encrypted_sym_key_path = encrypted_sym_key_path
        self.decrypted_text_path = decrypted_text_path
    
    def decrypt_data(self):
        with open(self.encrypted_text_path, "rb") as encrypted_text_file:
            ciphertext = encrypted_text_file.read()

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

        cipher = Cipher(algorithms.CAST5(sym_key), modes.CFB())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        with open(self.decrypted_text_path, "wb") as decrypted_text_file:
            decrypted_text_file.write(plaintext)