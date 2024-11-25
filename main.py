from logica import cifrar_proceso, descifrar_proceso
from interfaz import solicitar_datos_cifrar, solicitar_datos_descifrar

def main():
    print("Esquema de Secreto Compartido de Shamir")
    print("1. Cifrar documento")
    print("2. Descifrar documento")
    opcion = input("Selecciona una opción (1 o 2): ").strip()
    
    if opcion == '1':
        datos = solicitar_datos_cifrar()
        archivo_cifrado, archivo_fragmentos = cifrar_proceso(*datos)
        print(f"Archivo cifrado guardado como: {archivo_cifrado}")
        print(f"Fragmentos guardados en: {archivo_fragmentos}")
    
    elif opcion == '2':
        datos = solicitar_datos_descifrar()
        archivo_descifrado = descifrar_proceso(*datos)
        print(f"Archivo descifrado guardado como: {archivo_descifrado}")
    
    else:
        print("Opción no válida. Por favor selecciona 1 o 2.")

if __name__ == "__main__":
    main()
