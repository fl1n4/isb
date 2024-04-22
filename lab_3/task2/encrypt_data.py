import os
import logging

from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives import (hashes,
                                            padding,
                                            serialization)
from cryptography.hazmat.primitives.ciphers import (Cipher, 
                                                    algorithms, 
                                                    modes)


logging.basicConfig(level=logging.INFO)

class HybridEncryptor:
    """
    A class for encrypting data using hybrid encryption.

    This class provides methods for encrypting data from a text file using hybrid encryption.
    Hybrid encryption involves encrypting data symmetrically with a randomly generated key,
    and then encrypting that key asymmetrically using an RSA public key.

    Args:
        text_file_path (str): The file path of the plaintext data to be encrypted.
        private_key_path (str): The file path of the RSA private key used for decryption.
        encrypted_sym_key_path (str): The file path of the encrypted symmetric key.
        encrypted_text_path (str): The file path where the encrypted data will be saved.

    Methods:
        encrypt_data(self) -> None: Encrypts the data from the specified text file using hybrid encryption.
    """
    def __init__(self, text_file_path:str, private_key_path:str, encrypted_sym_key_path:str, encrypted_text_path:str) -> None:
        """
        Initialize the HybridEncryptor with file paths for encryption.

        Args:
            text_file_path (str): The file path of the plaintext data to be encrypted.
            private_key_path (str): The file path of the RSA private key used for decryption.
            encrypted_sym_key_path (str): The file path of the encrypted symmetric key.
            encrypted_text_path (str): The file path where the encrypted data will be saved.
        """
        self.text_file_path = text_file_path
        self.private_key_path = private_key_path
        self.encrypted_sym_key_path = encrypted_sym_key_path
        self.encrypted_text_path = encrypted_text_path
    
    def encrypt_data(self) -> None:
        """
        Encrypt the data from a text file using hybrid encryption.

        This method reads plaintext data from a text file specified by 'text_file_path'.
        It loads the RSA private key from the file specified by 'private_key_path'.
        It loads the encrypted symmetric key from the file specified by 'encrypted_sym_key_path'.
        The symmetric key is decrypted using the RSA private key.
        The data is encrypted using the decrypted symmetric key with CAST5 algorithm in CBC mode.
        The IV used for encryption is randomly generated.
        The encrypted data, along with the IV, is saved to the file specified by 'encrypted_text_path'.

        Raises:
            Any exceptions that occur during the encryption process are caught and logged using the logging module.

        Returns:
            None
        """
        try:
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
                asymmetric_padding.OAEP(
                    mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            iv = os.urandom(8)
            cipher = Cipher(algorithms.CAST5(sym_key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            padder = padding.PKCS7(128).padder()
            padded_text = padder.update(plaintext) + padder.finalize()
            ciphertext = iv + encryptor.update(padded_text) + encryptor.finalize()

            with open(self.encrypted_text_path, "wb") as encrypted_text_file:
                encrypted_text_file.write(ciphertext)
        except Exception as ex:
            logging.error(f"An error occurred while encrypting the text: {ex}")