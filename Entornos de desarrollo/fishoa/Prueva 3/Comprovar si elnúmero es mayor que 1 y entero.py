def es_numero_entero (num_player): #creamos un método para la gente que mete números en vez de palabras
    # creamos una variable que guarde el número que dice el jugador

    es_entero = False #variable que dice si es verdad que es entero

    try:  # con el try podemos comprobar si da error el código que le ponemos dentro
        int(num_player)
        # Si no hay error, significa que lo que ha escrito el jugador es un número
        es_entero = True
    # Si hay un error, significa que lo que ha escrito el jugador no es un número
    except ValueError:
        es_entero = False

    return es_entero




def las_palabras_encadenadas (): #creamos nuestro método con el juego
    #guardamos el número de jugadores
    num_player = input("cuántos jugadores sois: ")
    # y nos aseguremos que sea un número entero
    es_entero = es_numero_entero(num_player)
    # mientras que lo que haya metido en num_player no sea un número le volveremos a pedir un número
    while es_entero == False or num_player == "1" :
        num_player = input("Ponga un número distinto a 1, por favor: ")
        es_entero = es_numero_entero(num_player)
        if es_entero == True and num_player != "1":
            break
    # cuando el número sea entero, lo pasamos a int (entero)
    num_player = int(num_player)

las_palabras_encadenadas()