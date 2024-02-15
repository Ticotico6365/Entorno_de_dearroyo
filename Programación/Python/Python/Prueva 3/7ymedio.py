import random

def es_numero_entero (num_player): #creamos un método para la gente que mete números en vez de palabras

    es_entero = False #variable que dice si es verdad que es entero

    try:  # con el try podemos comprobar si da error el código que le ponemos dentro
        int(num_player)
        # Si no hay error, significa que lo que ha escrito el jugador es un número
        es_entero = True
    # Si hay un error, significa que lo que ha escrito el jugador no es un número
    except ValueError:
        es_entero = False

    return es_entero

def crear_baraja (): #creamos un método que haga barajas de cartas barajadas
    #definimos las propiedades de las cartas y una plantilla de carta
    tipo = [1, 2, 3, 4, 5, 6, 7, "Sota", "Caballo", "Rey"]
    palos = ["Oro", "Basto", "Copa", "Espadas"]
    carta = {
        "tipo": "",
        "palo": "",
        "valor": 0.0
    }
    #creamos la baraja que se creará
    baraja = []
    for i in palos:
        for j in tipo:
            carta_nueva = carta.copy()
            carta_nueva["tipo"] = j
            carta_nueva["palo"] = i
            baraja.append(carta_nueva)
    #barajamos la baraja
    random.shuffle(baraja)

    return baraja

def sieteYmedio (num_player):
    #creamos una variable para guardar la baraja
    baraja = crear_baraja()
    #creamos los mazos de los jugadores
    mazos = []
    #creamos la puntuación que lleva cada jugador
    contador = []

    while len(baraja) > 0:
        for i in range(num_player):
            mazos[i].append(baraja[-1])
            baraja.pop(-1)
            if mazos[i]["tipo"] == 1:
                contador[i] += 1
            elif mazos[i]["tipo"] == 2:
                contador[i] += 2
            elif mazos[i]["tipo"] == 3:
                contador[i] += 3
            elif mazos[i]["tipo"] == 4:
                contador[i] += 4
            elif mazos[i]["tipo"] == 5:
                contador[i] += 5
            elif mazos[i]["tipo"] == 6:
                contador[i] += 6
            elif mazos[i]["tipo"] == 7:
                contador[i] += 7
            elif mazos[i]["tipo"] == "Sota":
                contador[i] += "Sota"
            elif mazos[i]["tipo"] == "Caballo":
                contador[i] += "Caballo"
            elif mazos[i]["tipo"] == "Rey":
                contador[i] += "Rey"

sieteYmedio(3)