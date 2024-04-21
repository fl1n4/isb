import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import (hashes,
                                            padding,
                                            serialization)


def generate_hybrid_keys(sym_key_path, public_key_path, private_key_path):
    # Генерация ключа для симметричного алгоритма
    sym_key = os.urandom(16)
    
    # Генерация ключей для асимметричного алгоритма (RSA)
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    
    # Сериализация асимметричных ключей
    with open(public_key_path, "wb") as public_key_file:
        public_key_file.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    with open(private_key_path, "wb") as private_key_file:
        private_key_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))
    
    # Сериализация симметричного ключа
    with open(sym_key_path, "wb") as sym_key_file:
        sym_key_file.write(sym_key)
    
    # Зашифрование симметричного ключа открытым ключом и сохранение
    with open(public_key_path, "rb") as public_key_file:
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
    
    with open(sym_key_path, "wb") as sym_key_file:
        sym_key_file.write(encrypted_sym_key)