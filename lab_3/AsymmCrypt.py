from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import hashes


class AsymmCrypt:
    """
    Provides methods for asymmetric encryption and decryption using RSA algorithm.

    Methods:
        generate_key_pair(): Generates a pair of RSA private and public keys.
        encrypt_with_public_key(public_key: rsa.RSAPublicKey, sym_key: bytes) -> bytes:
            Encrypts a symmetric key with the provided RSA public key.
        decrypt_with_private_key(private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:
            Decrypts a ciphertext with the provided RSA private key.
    """
    
    def generate_key_pair(self) -> tuple:
        """
        Generates a pair of RSA private and public keys.

        Returns:
            tuple: A tuple containing RSA private key and public key.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        return private_key, public_key
    
    def encrypt_with_public_key(self, public_key: rsa.RSAPublicKey, sym_key: bytes) -> bytes:
        """
        Encrypts a symmetric key with the provided RSA public key.

        Args:
            public_key (rsa.RSAPublicKey): RSA public key used for encryption.
            sym_key (bytes): Symmetric key to be encrypted.

        Returns:
            bytes: Encrypted symmetric key.
        """

        encrypted_sym_key = public_key.encrypt(
                sym_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            ) 
        return encrypted_sym_key
    
    def decrypt_with_private_key(self, private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:
        """
        Decrypts a ciphertext with the provided RSA private key.

        Args:
            private_key (rsa.RSAPrivateKey): RSA private key used for decryption.
            ciphertext (bytes): Ciphertext to be decrypted.

        Returns:
            bytes: Decrypted text.
        """
        decrypted_text = private_key.decrypt(
                ciphertext,
                padding.OAEP(
                    mgf = padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        return decrypted_text