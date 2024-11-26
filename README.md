# **Esquema de Secreto Compartido de Shamir**

Esta aplicación proporciona una solución eficiente y práctica para cifrar y descifrar archivos mediante el **Esquema de Shamir** de manera que permite dividir una contraseña para un archivo cifrado en fragmentos y especificar un número mínimo de ellos para reconstruir y recuperar la contraseña y el archivo original.

---

## **Características Principales**

### **Cifrado de Archivos**
- Cifra archivos sensibles utilizando una contraseña proporcionada por el usuario.
- Genera un número `n` de fragmentos que representan las "partes del secreto".
- Permite configurar el número de personal minimo `t` necesario para la reconstrucción.

### **Descifrado de Archivos**
- Reconstruye y descifra el archivo original utilizando al menos `t` fragmentos válidos.
- Garantiza la integridad y seguridad de los datos durante el proceso de recuperación.

### **Interfaz de Usuario Intuitiva**
- Selección de archivos mediante cuadros de diálogo interactivos.
- Retroalimentación clara con mensajes de éxito y error para guiar al usuario.

---

## **Requisitos del Sistema**

- **Python**: Versión 3.7 o superior.
- **Librerías necesarias**:
  - `tkinter` para la interfaz gráfica. (incluida por defecto en Python).
  - `pycryptodome` para manejo de cifrado AES.
  - `hashlib` para generación de claves seguras (SHA-256).

---

## **Instrucciones de Instalación**

### **1. Clonar el Repositorio**
```bash
git clone https://github.com/Dani-Mol/Shamir_Secret_Sharing_Scheme.git
cd Shamir_Secret_Sharing_Scheme
```

### **2. Crear un Entorno Virtual (Recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### **3. Ejecutar la Aplicación**
```bash
python interfaz.py
```
```bash
python3 interfaz.py
```

---

## **Guía de Uso**

### **1. Cifrado**
1. Abre la aplicación y selecciona **"Cifrar Archivo"**.
2. Proporciona los siguientes elementos:
   - **Archivo Original**: Selecciona el archivo que deseas cifrar.
   - **Archivo Cifrado**: Define el nombre y la ubicación del archivo cifrado resultante.
   - **Archivo de Fragmentos**: Define el nombre y la ubicación para guardar los fragmentos generados.
3. Especifica:
   - `n`: Número total de fragmentos.
   - `t`: Número mínimo de fragmentos requeridos para descifrar.
4. Ingresa una contraseña segura cuando se solicite.
5. La aplicación generará el archivo cifrado y sus fragmentos.

### **2. Descifrado**
1. Abre la aplicación y selecciona **"Descifrar Archivo"**.
2. Proporciona los siguientes elementos:
   - **Archivo de Fragmentos**: Selecciona el archivo que contiene los fragmentos necesarios.
   - **Archivo Cifrado**: Selecciona el archivo previamente cifrado.
   - **Archivo Descifrado**: Define el nombre y la ubicación del archivo reconstruido.
3. La aplicación reconstruirá el archivo original y lo almacenará en la ubicación especificada.

---

## **Validaciones Importantes**

- **Requisitos de `n` y `t`**:
  - `n > 2`
  - `1 < t ≤ n`
- La contraseña es obligatoria para el cifrado de los datos.
- Se debe proporcionar un archivo válido en cada campo requerido para completar las operaciones.

---

## **Estructura del Proyecto**
- **`aes_cifrado.py`**: Contiene la implementación de la lógica cifrado y descifrado de documentos mediante SHA-256.
- **`interfaz.py`**: Contiene la implementación de la interfaz gráfica de usuario.
- **`logica.py`**: Encargado de hacer el cifrado y descifrado mediante el esquema de Shamir.
- **`shamir.py`**: Contiene la implementación de la lógica del esquema de Shamir.
- **`README.md`**: Documentación completa del proyecto.

---

## **Ejemplo de Flujo de Trabajo**

1. **Cifrado**:
   - Archivo original: `confidencial.txt`
   - Fragmentos generados: `fragmentos.frg`
   - Archivo cifrado: `confidencial.aes`
   - Fragmentos requeridos: 3 de 5.

2. **Descifrado**:
   - Archivo cifrado: `confidencial.aes`
   - Fragmentos disponibles: `fragmentos.frg` (3 fragmentos mínimos).
   - Archivo reconstruido: `confidencial_recuperado.txt`.

