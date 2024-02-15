
# 0 1 2
# 3 4 5
# 6 7 8

def pintar_tablero(tablero):
    print(tablero[0:3])
    print(tablero[3:6])
    print(tablero[6:9])

def gana_partida(tablero,num_jugador):

    simbolos = ["X", "O"]
    simbolo = simbolos[num_jugador]


    if tablero[0:3] == [simbolo, simbolo, simbolo]:
        return True
    elif tablero[3:6] == [simbolo, simbolo, simbolo]:
        return True
    elif tablero[6:9] == [simbolo, simbolo, simbolo]:
        return True
    elif tablero[0] == simbolo and tablero[3] == simbolo and tablero[6] == simbolo :
        return True
    elif tablero[1] == simbolo and tablero[4] == simbolo and tablero[7] == simbolo:
        return True
    elif tablero[2] == simbolo and tablero[5] == simbolo and tablero[8] == simbolo:
        return True
    elif tablero[0] == simbolo and tablero[4] == simbolo and tablero[8] == simbolo:
        return True
    elif tablero[2] == simbolo and tablero[4] == simbolo and tablero[6] == simbolo:
        return True
    else:
        return  False


def posicion_valida(tablero, posicion):
    return posicion in tablero


def sustituir_posicion(tablero,num_jugador,posicion):
    simbolos = ["X", "O"]
    tablero[posicion] = simbolos[num_jugador]


def tres_e_raya():
    #Montar / Dejar preparado el tablero
    tablero_unico = [0,1,2,3,4,5,6,7,8]

    #Pedir el nombre a los 2 jugadores
    nombres = []
    for i in range(2):
        nombres.append(input("Dime tu nombre:"))

    contador_turnos = 0

    #Empezamos las rondas por turnos
    while contador_turnos != 9:

        for i in range(2):
            #Pintamos tablero
            pintar_tablero(tablero_unico)

            #Subimos el contador de turnos
            contador_turnos +=1

            #Pedimos al jugador una posición del tablero
            posicion = int(input("Dime una posicion " + nombres[i] + " :"))
            while not posicion_valida(tablero_unico, posicion):
                posicion = int(input("Dime una posicion " + nombres[i] + " :"))

            #Sustituir la posición que nos ha dicho
            sustituir_posicion(tablero_unico, i, posicion)

            #Comprobar si el jugador gana con el movimiento
            if gana_partida(tablero_unico,i):
                pintar_tablero(tablero_unico)
                print("Jugador " + nombres[i] + " has ganado!")
                return
            elif contador_turnos == 9:
                break

    else:
        pintar_tablero(tablero_unico)
        print("HAY EMPATE")


tres_e_raya()