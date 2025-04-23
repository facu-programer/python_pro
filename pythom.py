var = True
diccionario = {
    "CRINGE": "algo embarasoso"
}
while var:
    var2 = input("escribe la palabra\n")
    if var2 in diccionario.keys():
        print(f"la definicion es: {diccionario[var2]}")
        break
    else:
        print("no se encuentra la palabra")