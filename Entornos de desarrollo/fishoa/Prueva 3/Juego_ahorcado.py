import random

def ahorcado ():
    #ponemos las palabras posibles en una lista
    palabras_ocultas = ["Pedro", "Pitagoras", "Ruffini", "Gauss", "fffffffff"]
    # Creamos una variable llamada palabra oculta, que es una palabra con un índice aleatorio.
    palabra_oculta = str(palabras_ocultas[random.randint(0,len(palabras_ocultas) - 1)]).lower()
    #Creamos lista con los giones de la palabra oculta
    palabra_vacia = []
    print(palabra_oculta)
    for i in range(len(palabra_oculta)):
        palabra_vacia += "_"
    print(palabra_vacia)
    #ponemos las vidas
    vida = 6
    """
    empezamos la partida
    """
    #creamos el bucle
    while vida != 0:
        letra = input("inserte su letra: ").lower()
        if len(letra) != 1:
            letra = input("inserte una letra: ")
        elif letra in palabra_oculta:
            for i in range(palabra_oculta.count(letra)):
                palabra_vacia.pop(palabra_oculta.index(letra))
                palabra_vacia.insert(palabra_oculta.index(letra), letra)

            print (palabra_vacia)

ahorcado()