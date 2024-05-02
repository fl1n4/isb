from cryptography.hazmat.primitives import serialization


class HelpFunc:

    def serialization_public_key(public_key:bytes, public_key_path:str) -> None:
        with open(public_key_path, "wb") as public_key_file:
            public_key_file.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))
            
    def serialization_private_key(private_key:bytes, private_key_path:str) -> None:
        with open(private_key_path, "wb") as private_key_file:
            private_key_file.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
    ))   
            
    def deserialization_public_key(public_key:bytes, public_key_path:str) -> None:
         with open(public_key_path, "rb") as public_key_file:
                public_key = serialization.load_pem_public_key(
                    public_key_file.read(),
                    password=None
                )
    def write_to_file(sym_key_path:str,encrypted_sym_key:bytes) -> None:
         with open(sym_key_path, "wb") as sym_key_file:
            sym_key_file.write(encrypted_sym_key)