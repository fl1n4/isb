import logging

from cryptography.hazmat.primitives.asymmetric import padding as asymetric_padding
from cryptography.hazmat.primitives import (hashes,
                                            padding,
                                            serialization)
from cryptography.hazmat.primitives.ciphers import (Cipher, 
                                                    algorithms, 
                                                    modes)


logging.basicConfig(level=logging.INFO)

class HybridDecryptor:
    """
    A class for decrypting data using hybrid decryption.

    This class provides methods for decrypting data from an encrypted text file using hybrid decryption.
    Hybrid decryption involves decrypting the symmetric key using an RSA private key,
    and then decrypting the data symmetrically using the decrypted key.

    Args:
        encrypted_text_path (str): The file path of the encrypted data to be decrypted.
        private_key_path (str): The file path of the RSA private key used for decryption.
        encrypted_sym_key_path (str): The file path of the encrypted symmetric key.
        decrypted_text_path (str): The file path where the decrypted data will be saved.

    Methods:
        decrypt_data(self) -> None: Decrypts the data from the specified encrypted text file using hybrid decryption.
    """
    def __init__(self, encrypted_text_path:str, private_key_path:str, encrypted_sym_key_path:str, decrypted_text_path:str) -> None:
        """
        Initialize the HybridDecryptor with file paths for decryption.

        Args:
            encrypted_text_path (str): The file path of the encrypted data to be decrypted.
            private_key_path (str): The file path of the RSA private key used for decryption.
            encrypted_sym_key_path (str): The file path of the encrypted symmetric key.
            decrypted_text_path (str): The file path where the decrypted data will be saved.
        """
        self.encrypted_text_path = encrypted_text_path
        self.private_key_path = private_key_path
        self.encrypted_sym_key_path = encrypted_sym_key_path
        self.decrypted_text_path = decrypted_text_path
    
    def decrypt_data(self) -> None:
        """
        Decrypt the data from an encrypted text file using hybrid decryption.

        This method reads ciphertext data from an encrypted text file specified by 'encrypted_text_path'.
        It loads the RSA private key from the file specified by 'private_key_path'.
        It loads the encrypted symmetric key from the file specified by 'encrypted_sym_key_path'.
        The symmetric key is decrypted using the RSA private key.
        The data is decrypted using the decrypted symmetric key with CAST5 algorithm in CBC mode.
        The IV used for decryption is extracted from the beginning of the ciphertext.
        The decrypted data is unpadded and saved to the file specified by 'decrypted_text_path'.

        Raises:
            Any exceptions that occur during the decryption process are caught and logged using the logging module.

        Returns:
            None
        """
        try:
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
                asymetric_padding.OAEP(
                    mgf = asymetric_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            iv = ciphertext[:8]
            ciphertext = ciphertext[8:]
            cipher = Cipher(algorithms.CAST5(sym_key), modes.CBC(iv))
            decryptor = cipher.decryptor()

            plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            unpadder = padding.PKCS7(128).unpadder()
            plaintext = unpadder.update(plaintext) + unpadder.finalize()

            with open(self.decrypted_text_path, "wb") as decrypted_text_file:
                decrypted_text_file.write(plaintext)
        except Exception as ex:
            logging.error(f"An error occurred while decrypting the text: {ex}")