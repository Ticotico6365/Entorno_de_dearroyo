def palabras_encadenadas():

    #Preguntar por el número de jugadores
    num_jugadores = int(input("Dime el número de jugadores:"))

    #Preguntar el nombre de cada uno de los jugadores
    nombres = []
    for i in range(num_jugadores):
        nombres.append(input("Dime el nombre del jugador:"))


    palabra_anterior = ""
    palabras_dichas = []

    #Mientras la palabra que se diga empiece por
    #las dos ultimas letra de la palabra anterior
    while True:
        for jugador in nombres:
            palabra_dicha = input("Dime una palabra " + jugador + " :")
            if palabra_anterior == "" or (palabra_dicha[:2] == palabra_anterior[-2:] and palabra_dicha not in palabras_dichas):
                palabra_anterior = palabra_dicha
                palabras_dichas.append(palabra_dicha)
            else:
                print("Has perdidio " + jugador)
                return





palabras_encadenadas()