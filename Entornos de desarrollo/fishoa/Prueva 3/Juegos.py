import random #llamamos al método random, para que nos de la posibilidad de generar números aleatorios
def quita_numero (text): #creamos un método para que nos quite lo que está fuera del alfabeto
    for i in text:
        if i.isalpha() or i.isspace():  #isalpha comprueva todas las vocales y isspace comprueva los espacios.
            text.replace(i,"")
    return text
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

def adivina_el_numero_secreto (): #creamos nuestro método con el juego
    #creamos variable donde se guardará el número secreo
    num_secret = random.randint (1,10)

    #guardamos el nombre del jugador
    name_player = input("dime su nombre jugador: ")

    #damos la bienvenida al jugador
    print("bienvenido", name_player, "ahora mismo estoy pensando en un número del 1 al 10, que usted debe de adivinar, pero solo tendrá 3 intentos. Buena suerte")

    #creamos la variable onde se guardan las vidas del jugador
    vida = 3

    #guardamos los intentos
    intentos = 0

    while vida != 0:
        intentos += 1
        vida -= 1
        #guardamos el número del jugador
        num_player = input("Ponga su número: ")
        #y nos aseguremos que sea un número entero
        es_entero = es_numero_entero(num_player)
        #mientras que lo que haya metido el jugador no sea un número le volveremos a pedir un número
        while es_entero == False:
            num_player = input("Ponga su número: ")
            es_entero = es_numero_entero(num_player)
            if es_entero == True:
                break
        #cuando el número sea entero, lo pasamos a int
        num_player = int(num_player)
        #comprovamos en el caso que haya fallado si el número es mayor
        if num_player > num_secret:
            print("su número es mayor que el que pienso")

        #comprovamos en el caso que haya fallado si el número es menor
        elif num_player < num_secret:
            print("su número es menor que el que pienso")

        #comprovamos si el número del jugador es igual que el del programa
        elif num_player == num_secret:
            print("!!!ENHORABUENA¡¡¡ Has adivinado el número que estaba pensando, el ",num_player, "  Lo has hecho en ", intentos,"intentos y te has quedado a ", vida, "vidas")
            break
    if vida == 0:
        print ("Has perdido, buena suerte a la próxima")

#adivina_el_numero_secreto()


def las_palabras_encadenadas (): #creamos nuestro método con el juego
    """
    preparamos el inicio del juego
    """
    #guardamos el número de jugadores
    num_player = input("cuántos jugadores sois: ")
    # y nos aseguremos que sea un número entero
    es_entero = es_numero_entero(num_player)
    # mientras que lo que haya metido en num_player no sea un número entero diferente a 1 le volveremos a pedir un número
    while es_entero == False or num_player == "1" :
        num_player = input("Ponga un número distinto a 1, por favor: ")
        es_entero = es_numero_entero(num_player)
        #cuando el jugador sea bueno nos salimos del bucle
        if es_entero == True and num_player != "1":
            break

    # cuando el número sea entero, lo pasamos a int (entero)
    num_player = int(num_player)

    #guardamos los nombres de los jugadores en una lista
    players = []
    #guardamos el orden de los jugadores, para nombrarlos
    contador = 0
    # pedimos los nombres de los jugadores según el número de jugadores que haya
    for i in range(num_player):
        contador += 1
        print("Digame su nombre player", contador, ":")
        players.append(input())

    """
    Creamos las variables con las palabras
    """
    # Guardamos las palabras dichas en una lista
    palabras_dichas = [""]
    # hacemos una variable que en un futuro guarde la palabra que dice el jugador
    palabra_nueva = ""
    #hacemos una variable que en un futuro guarde la última palabra
    palabra_fin = palabras_dichas
    """
    Empezamos con las normas del juego
    """
    #mientars que ninguna de las 2 condiciones no se cumplan el programa preguntará por la palabra
    while palabra_fin[-2:] != palabra_nueva[:2] or palabras_dichas.count(palabra_nueva) == 1:

        #creamos un for para que valla haciendo la partida por turnos
        for j in range(num_player):
            #vamos pidiendo las palabras
            print("Diga su palabra jugador",players[j],":")
            palabra_nueva = quita_numero(input().lower())
            #la palabra fin es la última palabra
            palabra_fin = palabras_dichas[-1]
            #insertamos la última palabra en la lista de palabras
            palabras_dichas.append(palabra_nueva)
            #vemos si se repite dentro del turno, para que se salga del bucle de los turnos
            if palabras_dichas.count(palabra_nueva) == 2 or (j >= 1 and palabra_fin[-2:] != palabra_nueva[:2]) :
                break
        # vemos si se repite dentro de la partida, para que aparezca del mensaje de error
        if palabras_dichas.count(palabra_nueva) == 2 or palabra_fin[-2:] != palabra_nueva[:2]:
            break
    print("El jugador", players[j], "ha fallado")

#las_palabras_encadenadas()
