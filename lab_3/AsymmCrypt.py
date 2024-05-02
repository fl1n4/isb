from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import hashes

class AsymmCrypt:
    def generate_key_pair(self) -> tuple:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        return private_key, public_key
    
    def encrypt_with_public_key(self, public_key: rsa.RSAPublicKey, sym_key: bytes) -> bytes:
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
        decrypted_text = private_key.decrypt(
                ciphertext,
                padding.OAEP(
                    mgf = padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        return decrypted_text