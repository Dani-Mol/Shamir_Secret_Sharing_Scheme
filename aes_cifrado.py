from Crypto.Cipher import AES

# Constantes
NONCE_SIZE = 16
TAG_SIZE = 16

def cifrar_documento(archivo_claro, archivo_cifrado, clave):
    """
    Cifra un archivo utilizando AES.
    Args:
        archivo_claro (str): Ruta del archivo original.
        archivo_cifrado (str): Ruta del archivo cifrado.
        clave (str): Clave de 256 bits (en formato hexadecimal).
    """
    if len(clave) != 64:
        raise ValueError("La clave debe ser de 256 bits (64 caracteres hexadecimales).")

    clave_bytes = bytes.fromhex(clave)
    cipher = AES.new(clave_bytes, AES.MODE_EAX)
    nonce = cipher.nonce

    try:
        with open(archivo_claro, 'rb') as archivo:
            datos = archivo.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo original: {archivo_claro}")

    datos_cifrados, tag = cipher.encrypt_and_digest(datos)

    with open(archivo_cifrado, 'wb') as archivo:
        archivo.write(nonce)           # Nonce
        archivo.write(tag)             # Tag
        archivo.write(datos_cifrados)  # Datos cifrados

    print(f"Archivo cifrado correctamente: {archivo_cifrado}")


def descifrar_documento(archivo_cifrado, archivo_descifrado, clave):
    """
    Descifra un archivo cifrado con AES y guarda el resultado.
    Args:
        archivo_cifrado (str): Ruta del archivo cifrado.
        archivo_descifrado (str): Ruta del archivo descifrado.
        clave (str): Clave de 256 bits (en formato hexadecimal).
    """
    if len(clave) != 64:
        raise ValueError("La clave debe ser de 256 bits (64 caracteres hexadecimales).")

    clave_bytes = bytes.fromhex(clave)

    try:
        with open(archivo_cifrado, 'rb') as f:
            nonce = f.read(NONCE_SIZE)
            tag = f.read(TAG_SIZE)
            datos_cifrados = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo cifrado: {archivo_cifrado}")
    except Exception as e:
        raise Exception(f"Error al leer el archivo cifrado: {str(e)}")

    try:
        cipher = AES.new(clave_bytes, AES.MODE_EAX, nonce=nonce)
        datos_descifrados = cipher.decrypt_and_verify(datos_cifrados, tag)
    except ValueError:
        raise ValueError("Error al descifrar: La clave es incorrecta o los datos están corruptos.")

    with open(archivo_descifrado, 'wb') as f:
        f.write(datos_descifrados)

    print(f"Archivo descifrado correctamente. Guardado en: {archivo_descifrado}")
