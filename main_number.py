import random
var_min = 0
var_max = 100


def main2():
    global var_min

    global var_max
    var_min = input("elige el minimo del rango del numero: ")
    var_max = input("elige el maximo del rango del numero: ")
    try:
        var_min = int(var_min)
        var_max = int(var_max)
        if var_min > var_max:
            print("el minimo no puede ser mayor que el maximo")
            main2()
    except:
        print("no es un numero")
        main2()
main2()
def main():
        var77 = True
        while var77:
           var = input("elige un numero: ")
           try:
                if var == "depuration_mode":
                    print("modo depuracion activado")
                    print("el numero es: ", var2)
                var = int(var)
                var77 = False
           except Exception as e:
               print("no es un numero")
        return var
var2 = random.randint(var_min, var_max)
var = main()

while True:
    if var == var2:
        print("ganaste")
        def basic():
             var3 = input("quieres jugar de nuevo? (s/n): ").strip().lower()
             if var3 == "s":
                global var
                global var2
                var2 = random.randint(var_min, var_max)
                var = main()

             elif var3 == "n":
                  return True
             else:
                 print("no es una respuesta valida")
                 basic()
        if basic():
            break
    elif int(var) > var2:
        print("el numero es menor")
        var = main()
    elif int(var) < var2:
        print("el numero es mayor")
        var = main()