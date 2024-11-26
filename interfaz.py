import tkinter as tk
from tkinter import filedialog, messagebox
from logica import cifrar_proceso, descifrar_proceso

class AplicacionShamir:
    def __init__(self, root):
        self.root = root
        self.root.title("Esquema de Shamir")
        self.root.geometry("400x300")
        self.root.config(bg="#252525")

        # Título
        tk.Label(self.root, text="Esquema de Shamir", font=("Helvetica", 16), bg="#252525").pack(pady=20)

        # Botones
        tk.Button(self.root, text="Cifrar Archivo", command=self.abrir_cifrado, bg="#87cefa", font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Descifrar Archivo", command=self.abrir_descifrado, bg="#87cefa", font=("Arial", 12)).pack(pady=10)

    def abrir_cifrado(self):
        VentanaCifrado(self.root)

    def abrir_descifrado(self):
        VentanaDescifrado(self.root)

class VentanaCifrado:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Cifrar Archivo")
        self.win.geometry("400x400")
        self.win.focus_force()

        # Título y texto
        tk.Label(self.win, text="Cifrar Archivo", font=("Helvetica", 14)).pack(pady=10)
        
        # Campos para la entrada de archivos
        self.archivo_claro = None
        self.archivo_cifrado = None
        self.archivo_fragmentos = None

        tk.Button(self.win, text="Seleccionar archivo claro", command=self.seleccionar_archivo_claro).pack(pady=5)
        tk.Button(self.win, text="Seleccionar archivo para guardar cifrado", command=self.seleccionar_archivo_cifrado).pack(pady=5)
        tk.Button(self.win, text="Seleccionar archivo para fragmentos", command=self.seleccionar_archivo_fragmentos).pack(pady=5)

        # Campos para t y n
        tk.Label(self.win, text="Número de fragmentos (n):").pack(pady=5)
        self.entry_n = tk.Entry(self.win)
        self.entry_n.pack(pady=5)

        tk.Label(self.win, text="Número mínimo de fragmentos para descifrar (t):").pack(pady=5)
        self.entry_t = tk.Entry(self.win)
        self.entry_t.pack(pady=5)

        # Botón para iniciar cifrado
        tk.Button(self.win, text="Cifrar", command=self.iniciar_cifrado, bg="#32CD32").pack(pady=10)

    def seleccionar_archivo_claro(self):
        self.archivo_claro = filedialog.askopenfilename(title="Seleccionar archivo claro", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
        if self.archivo_claro:
            print(f"Archivo claro seleccionado: {self.archivo_claro}")

    def seleccionar_archivo_cifrado(self):
        self.archivo_cifrado = filedialog.asksaveasfilename(defaultextension=".aes", title="Seleccionar archivo cifrado", filetypes=(("Archivos AES", "*.aes"), ("Todos los archivos", "*.*")))
        if self.archivo_cifrado:
            print(f"Archivo cifrado guardado como: {self.archivo_cifrado}")

    def seleccionar_archivo_fragmentos(self):
        self.archivo_fragmentos = filedialog.asksaveasfilename(defaultextension=".frg", title="Seleccionar archivo para fragmentos", filetypes=(("Archivos de fragmentos", "*.frg"), ("Todos los archivos", "*.*")))
        if self.archivo_fragmentos:
            print(f"Archivo de fragmentos guardado como: {self.archivo_fragmentos}")

    def iniciar_cifrado(self):
        try:
            n = int(self.entry_n.get())
            t = int(self.entry_t.get())

            if n <= 2 or t <= 1 or t > n:
                raise ValueError("El número de fragmentos (n) debe ser mayor que 2 y el número mínimo de fragmentos (t) debe ser mayor que 1 y menor o igual a n.")

            if not self.archivo_claro or not self.archivo_cifrado or not self.archivo_fragmentos:
                raise ValueError("Debe seleccionar todos los archivos necesarios.")

            contraseña = self.obtener_contraseña()
            if contraseña:
                cifrar_proceso(n, t, self.archivo_claro, self.archivo_fragmentos, self.archivo_cifrado, contraseña)
                messagebox.showinfo("Cifrado Completo", "El archivo ha sido cifrado exitosamente y los fragmentos generados.")
                self.win.destroy()
            else:
                raise ValueError("La contraseña es requerida.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cifrar: {str(e)}")

    def obtener_contraseña(self):
        contraseña_ventana = tk.Toplevel(self.win)
        contraseña_ventana.title("Ingrese la contraseña")
        contraseña_ventana.geometry("300x150")
        
        tk.Label(contraseña_ventana, text="Contraseña (sin eco):").pack(pady=5)
        entry_contraseña = tk.Entry(contraseña_ventana, show="*")
        entry_contraseña.pack(pady=5)
        
        def confirmar_contraseña():
            contraseña_ventana.quit()
            return entry_contraseña.get()

        tk.Button(contraseña_ventana, text="Aceptar", command=confirmar_contraseña).pack(pady=10)
        contraseña_ventana.mainloop()
        return entry_contraseña.get()

class VentanaDescifrado:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Descifrar Archivo")
        self.win.geometry("400x400")
        self.win.focus_force()

        # Título y texto
        tk.Label(self.win, text="Descifrar Archivo", font=("Helvetica", 14)).pack(pady=10)
        
        # Campos para seleccionar archivos
        self.archivo_cifrado = None
        self.archivo_fragmentos = None
        self.archivo_descifrado = None

        tk.Button(self.win, text="Seleccionar archivo de fragmentos", command=self.seleccionar_archivo_fragmentos).pack(pady=5)
        tk.Button(self.win, text="Seleccionar archivo cifrado", command=self.seleccionar_archivo_cifrado).pack(pady=5)
        tk.Button(self.win, text="Seleccionar archivo para guardar descifrado", command=self.seleccionar_archivo_descifrado).pack(pady=5)

        # Botón para iniciar descifrado
        tk.Button(self.win, text="Descifrar", command=self.iniciar_descifrado, bg="#32CD32").pack(pady=10)

    def seleccionar_archivo_cifrado(self):
        self.archivo_cifrado = filedialog.askopenfilename(title="Seleccionar archivo cifrado", filetypes=(("Archivos AES", "*.aes"), ("Todos los archivos", "*.*")))
        if self.archivo_cifrado:
            print(f"Archivo cifrado seleccionado: {self.archivo_cifrado}")

    def seleccionar_archivo_fragmentos(self):
        self.archivo_fragmentos = filedialog.askopenfilename(title="Seleccionar archivo de fragmentos", filetypes=(("Archivos de fragmentos", "*.frg"), ("Todos los archivos", "*.*")))
        if self.archivo_fragmentos:
            print(f"Archivo de fragmentos seleccionado: {self.archivo_fragmentos}")

    def seleccionar_archivo_descifrado(self):
        self.archivo_descifrado = filedialog.asksaveasfilename(defaultextension=".txt", title="Seleccionar archivo para guardar el documento descifrado", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
        if self.archivo_descifrado:
            print(f"Archivo descifrado guardado como: {self.archivo_descifrado}")

    def iniciar_descifrado(self):
        try:
            if not self.archivo_cifrado or not self.archivo_fragmentos or not self.archivo_descifrado:
                raise ValueError("Debe seleccionar todos los archivos necesarios.")

            with open(self.archivo_fragmentos, 'r') as f:
                fragmentos = f.readlines()

            descifrar_proceso(fragmentos, self.archivo_cifrado, self.archivo_descifrado)
            messagebox.showinfo("Descifrado Completo", "El archivo ha sido descifrado exitosamente.")
            self.win.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error al descifrar: {str(e)}")

# Ejecutar la interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionShamir(root)
    root.mainloop()
    