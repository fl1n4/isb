import os
import logging

from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import (hashes,
                                            serialization)


logging.basicConfig(level=logging.INFO)

class HybridKeyGenerator:
    """
    A class for generating and managing hybrid encryption keys.

    This class provides methods for generating a symmetric key and an RSA key pair,
    encrypting the symmetric key with the RSA public key, and saving the keys to files.

    Args:
        sym_key_path (str): The file path where the encrypted symmetric key will be saved.
        public_key_path (str): The file path where the RSA public key will be saved.
        private_key_path (str): The file path where the RSA private key will be saved.

    Methods:
        generate_keys(self) -> None: Generates a symmetric key and RSA key pair,
            encrypts the symmetric key with the RSA public key, and saves them to files.
    """
    def __init__(self, sym_key_path:str, public_key_path:str, private_key_path:str) -> None:
        """
        Initialize the HybridKeyGenerator with file paths for keys.

        Args:
            sym_key_path (str): The file path where the encrypted symmetric key will be saved.
            public_key_path (str): The file path where the RSA public key will be saved.
            private_key_path (str): The file path where the RSA private key will be saved.
        """
        self.sym_key_path = sym_key_path
        self.public_key_path = public_key_path
        self.private_key_path = private_key_path
    
    def generate_keys(self) -> None:
        """
        Generate a symmetric key and RSA key pair, and save them to files.

        This method generates a random symmetric key using os.urandom() function.
        It also generates an RSA key pair with a specified public exponent and key size.
        The generated public key is saved to the specified public key file path.
        The generated private key is saved to the specified private key file path.
        The symmetric key is encrypted with the RSA public key and saved to the specified symmetric key file path.

        Raises:
            Any exceptions that occur during the key generation process are caught and logged using the logging module.

        Returns:
            None
        """
        try:
            sym_key = os.urandom(8)

            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048
            )
            public_key = private_key.public_key()

            with open(self.public_key_path, "wb") as public_key_file:
                public_key_file.write(public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))
            with open(self.private_key_path, "wb") as private_key_file:
                private_key_file.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                ))

            with open(self.public_key_path, "rb") as public_key_file:
                public_key = serialization.load_pem_public_key(
                    public_key_file.read()
                )
            
            encrypted_sym_key = public_key.encrypt(
                sym_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            
            with open(self.sym_key_path, "wb") as sym_key_file:
                sym_key_file.write(encrypted_sym_key)
        except Exception as ex:
            logging.error(f"An error occurred while generating the keys: {ex}")