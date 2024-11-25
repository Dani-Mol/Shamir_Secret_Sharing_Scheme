import hashlib
from aes_cifrado import cifrar_documento, descifrar_documento
from shamir import generar_polinomio, reconstruir_secreto

def cifrar_proceso(n, t, archivo_claro, archivo_fragmentos, archivo_cifrado, contraseña):
    sha256 = hashlib.sha256(contraseña.encode()).hexdigest()
    clave_cifrado = int(sha256, 16) % (2**256)
    fragmentos = generar_polinomio(clave_cifrado, n, t)

    with open(archivo_fragmentos, 'w') as f:
        for x, y in fragmentos:
            f.write(f"{x},{y}\n")

    cifrar_documento(archivo_claro, archivo_cifrado, sha256)

def descifrar_proceso(fragmentos, archivo_cifrado, archivo_descifrado):
    puntos = [tuple(map(int, linea.strip().split(','))) for linea in fragmentos]
    clave_reconstruida = reconstruir_secreto(puntos)
    sha256 = f"{clave_reconstruida:064x}"
    descifrar_documento(archivo_cifrado, archivo_descifrado, sha256)
