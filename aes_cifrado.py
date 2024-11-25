from Crypto.Cipher import AES
import os

def cifrar_documento(archivo_claro, archivo_cifrado, clave):
    """
    Cifra un archivo utilizando AES.
    Args:
        archivo_claro (str): Ruta del archivo original.
        archivo_cifrado (str): Ruta del archivo cifrado.
        clave (str): Clave de 256 bits (en formato hexadecimal).
    """
    clave_bytes = bytes.fromhex(clave)
    cipher = AES.new(clave_bytes, AES.MODE_EAX)
    nonce = cipher.nonce

    with open(archivo_claro, 'rb') as f:
        datos = f.read()

    datos_cifrados, tag = cipher.encrypt_and_digest(datos)

    with open(archivo_cifrado, 'wb') as f:
        f.write(nonce)
        f.write(tag)
        f.write(datos_cifrados)

def descifrar_documento(archivo_cifrado, archivo_descifrado, clave):
    """
    Descifra un archivo cifrado con AES.
    Args:
        archivo_cifrado (str): Ruta del archivo cifrado.
        archivo_descifrado (str): Ruta del archivo descifrado.
        clave (str): Clave de 256 bits (en formato hexadecimal).
    """
    clave_bytes = bytes.fromhex(clave)

    with open(archivo_cifrado, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        datos_cifrados = f.read()

    cipher = AES.new(clave_bytes, AES.MODE_EAX, nonce=nonce)
    datos = cipher.decrypt_and_verify(datos_cifrados, tag)

    with open(archivo_descifrado, 'wb') as f:
        f.write(datos)
