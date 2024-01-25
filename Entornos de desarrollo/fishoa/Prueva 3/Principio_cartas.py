import random
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


def reparte_cartas_todas(num_players, baraja):

    posibilidad = num_players <= len(baraja)
    mazos = []
    if posibilidad == False:
        return None
    for i in range(num_players):
        mazos.append([])

    while len(baraja) > 0:
        for i in range(num_players):
            mazos[i].append(baraja[-1])
            baraja.pop(-1)

    return mazos

def reparte_cartas (num_players,num_cartas,baraja):
    #vemos si se puede repartir las cartas
    posibilidad = num_cartas  * num_players <= len(baraja)
    #creamos los mazos de cada jugador
    mazos = []
    #si es posible repartir se reparte si no no
    if posibilidad:
        #recorremos los jugadores y vamos repartiendo las cartas que le corresponden a cada uno
        for i in range(num_players):
            mazos.append([baraja[:num_cartas]])
            baraja = baraja[num_cartas:]
    else:
        print("Números de jugadores o cartas no válido")

    return mazos
