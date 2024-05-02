from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


class HelpFunc:
    """
    Utility class providing helper functions for serialization, deserialization, and file I/O.
    """

    def serialization_public_key(self, public_key: bytes, public_key_path: str) -> None:
        """
        Serialize a public key to a file.

        Args:
            public_key (bytes): The public key bytes to be serialized.
            public_key_path (str): The path to save the serialized public key.
        """
        with open(public_key_path, "wb") as public_key_file:
            public_key_file.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))
            
    def serialization_private_key(self, private_key: bytes, private_key_path: str) -> None:
        """
        Serialize a private key to a file.

        Args:
            private_key (bytes): The private key bytes to be serialized.
            private_key_path (str): The path to save the serialized private key.
        """
        with open(private_key_path, "wb") as private_key_file:
            private_key_file.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
    ))   
            
    def deserialization_private_key(self, private_key_path: str) -> rsa.RSAPrivateKey:
        """
        Deserialize a private key from a file.

        Args:
            private_key_path (str): The path to the file containing the serialized private key.

        Returns:
            rsa.RSAPrivateKey: The deserialized RSA private key.
        """
        with open(private_key_path, "rb") as private_key_file:
                return serialization.load_pem_private_key(
                    private_key_file.read(),
                    password=None
                )
                
    def write_to_file(self, sym_key_path: str,encrypted_sym_key: bytes) -> None:
        """
        Write encrypted symmetric key bytes to a file.

        Args:
            sym_key_path (str): The path to save the encrypted symmetric key.
            encrypted_sym_key (bytes): The encrypted symmetric key bytes.
        """
        with open(sym_key_path, "wb") as sym_key_file:
            sym_key_file.write(encrypted_sym_key)
            
    def read_file(self, sym_key_path: str) -> bytes:
        """
        Read bytes from a file.

        Args:
            sym_key_path (str): The path to the file to be read.

        Returns:
            bytes: The bytes read from the file.
        """
        with open(sym_key_path, 'rb') as sym_key_file:
            return sym_key_file.read()