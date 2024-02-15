import random
#ponemos las condiciones con las que se determinan el valor de las cartas en el 7ymedio
def valor_carta (tipo):
    valor = 0
    #si es número entero devuelve True
    es_entero = isinstance(tipo, int)
    if es_entero == True:
        valor = tipo
    else:
        valor = 0.5
    return valor


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
            carta_nueva["valor"] = valor_carta(carta_nueva["tipo"])
            baraja.append(carta_nueva)
    #barajamos la baraja
    random.shuffle(baraja)

    return baraja
def sieteymedio ():
    #generamos la baraja
    baraja = crear_baraja()
    #preguntamos el número de jugadores
    num_players = int(input("inserte el número de jugadores: "))
    #creamos los mazos de los jugadores
    mazos = []
    #creamos la puntuación que lleva cada jugador
    contador = []
    for i in range(num_players):
        # según el número de jugadores que haya se crea un mazo para cada jugador
        mazos.append([])
        # añadimos las 3 puntuaciones
        contador.append([0])

    #creamos una variable donde guardar los deseos de los jugadores
    seguir = None
    #empieza el juego
    while True:
        seguir = input("Desearía usted seguir:")
        for i in range(num_players):
            # repartimos la primera carta para cada jugador
            mazos[i].append(baraja[-1])
            # eliminamos la carta de la baraja
            baraja.pop(-1)
            #metemos puntuación
            contador[i][0] += (contador[i][0] + mazos[i][0]["valor"])


sieteymedio()