from cryptography.hazmat.primitives import (hashes,
                                            padding,
                                            serialization)
from cryptography.hazmat.primitives.ciphers import (Cipher, 
                                                    algorithms, 
                                                    modes)


def decrypt_data_hybrid(encrypted_text_path, private_key_path, encrypted_sym_key_path, decrypted_text_path):
    # Чтение зашифрованного текста из файла
    with open(encrypted_text_path, "rb") as encrypted_text_file:
        ciphertext = encrypted_text_file.read()
    
    # Расшифрование симметричного ключа
    with open(private_key_path, "rb") as private_key_file:
        private_key = serialization.load_pem_private_key(
            private_key_file.read(),
            password=None,
        )
    
    with open(encrypted_sym_key_path, "rb") as encrypted_sym_key_file:
        encrypted_sym_key = encrypted_sym_key_file.read()
    
    sym_key = private_key.decrypt(
        encrypted_sym_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    # Расшифрование текста симметричным алгоритмом
    cipher = Cipher(algorithms.CAST5(sym_key), modes.CFB())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Сохранение расшифрованного текста
    with open(decrypted_text_path, "wb") as decrypted_text_file:
        decrypted_text_file.write(plaintext)