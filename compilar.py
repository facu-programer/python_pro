import subprocess
import tkinter as tk
from tkinter import filedialog
import os

def compilar_archivo(archivo):
    subprocess.run(f'nuitka "{archivo}"', shell=True, cwd=os.path.dirname(archivo))

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    archivo = filedialog.askopenfilename(
    title="Seleccionar archivo a compilar",
    filetypes=[("Archivos de python", "*.py"), ("Todos los archivos", "*.*")]
)
    print(archivo)
    if not archivo:
        print("No se seleccionó ningún archivo.")
        main()
        return
    subprocess.run(f'nuitka "{archivo}"', shell=True, cwd=os.path.dirname(archivo))
    print("Compilado en la carpeta del archivo")

if __name__ == "__main__":
    main()
    input("Presiona Enter para salir...")