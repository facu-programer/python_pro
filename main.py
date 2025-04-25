import random
import string
def generar_contraseña(longitud=12, lista=None):
    if lista is None:
        return "".join([random.choice(string.ascii_letters) for _ in range(longitud)])
    else:
        return "".join([random.choice(lista) for _ in range(longitud)])

__name__ = "__main__"
def main():
    texto = r"""|@#~€¬[{!"·$%&/()==?¿^¨**¨+`´+`ººª\\}]'"""
    lista = string.ascii_letters + string.digits + string.punctuation + "".join(texto)
    print("Generador de contraseñas")
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    contraseña = generar_contraseña(longitud, lista)
    print(f"Contraseña generada: {contraseña}")
if __name__ == "__main__":
    main()

while True:
    var = input("¿Desea generar otra contraseña? (s/n): ")
    if var.lower() == "s":
        main()
    elif var.lower() == "n":
        print("Gracias por usar el generador de contraseñas.")
        break
    else:
        print("Opción no válida. Por favor, ingrese 's' o 'n'.")
        continue