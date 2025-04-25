var = True
diccionario = {
    "cringe": "Algo que causa vergüenza ajena o incomodidad.",
    "random": "Alguien o algo fuera de lugar o inesperado.",
    "literal": "Usado para enfatizar algo, aunque no siempre de forma literal.",
    "vibes": "Energía o sensación que transmite algo o alguien.",
    "aesthetic": "Estilo visual o apariencia agradable.",
    "based": "Alguien que tiene opiniones firmes y no le importa lo que otros piensen.",
    "NPC": "Persona que parece actuar sin iniciativa propia, como un personaje no jugable.",
    "slay": "Hacer algo muy bien, destacar con confianza.",
    "bro": "Forma informal de referirse a alguien, sin importar género.",
    "no cap": "En serio, sin mentiras.",
    "cap": "Mentira o exageración.",
    "rizz": "Habilidad para coquetear o atraer a alguien.",
    "sus": "Sospechoso o raro.",
    "delulu": "Alguien que vive en una fantasía o se autoengaña.",
    "main character": "Alguien que actúa como si fuera el protagonista de una historia.",
    "sigma": "Persona que se mantiene independiente, centrada y con actitud fuerte.",
    "gyatt": "Exclamación al ver a alguien con mucho trasero.",
    "valid": "Algo aceptable o que se ve bien.",
    "mid": "Mediocre, no tan bueno como se esperaba.",
    "cheugy": "Fuera de moda o tratando demasiado de ser cool.",
    "bet": "Afirmación, como decir 'ok' o 'dale'.",
    "goofy": "Alguien tonto, pero de forma graciosa o inofensiva.",
    "yeet": "Lanzar algo con fuerza o entusiasmo.",
    "skibidi": "Palabra sin sentido usada en trends, generalmente para humor absurdo.",
    "gigachad": "Hombre extremadamente alfa, atractivo e idealizado.",
    "bussin": "Algo muy rico o extremadamente bueno.",
    "touch grass": "Consejo sarcástico para que alguien deje la compu y se conecte con la realidad.",
    "glow up": "Transformación positiva, especialmente en apariencia.",
    "finna": "Forma corta de 'going to', como decir 'voy a'.",
}

while True:
    var2 = input("escribe la palabra\n").strip().lower()
    if var2 in diccionario.keys():
        print(f"la definicion es: {diccionario[var2]}")
        var2 = input("quieres buscar otra palabra? (s/n)\n").strip().lower()
        if var2 == "s":
            continue
        elif var2 == "n":
            print("adios")
            break
        else:
            print("opcion no valida, sera tomada como si quieras buscar otra palabra")
    else:
        print("no se encuentra la palabra")
        print(f"las opciones son: {", ".join(diccionario.keys())}")
