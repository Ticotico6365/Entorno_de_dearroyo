import random
#Transatlantico -> 3 puntos
#Acorazado -> 4 puntos
#Submarino -> 5 puntos


def hundir_barcos():

    #Pedir a los jugadores los nombre
    jugadores = []
    for i in range(2):
        jugadores.append(input("Dime tu nombre:"))

    #marcadores
    marcador_j1 = 0
    marcador_j2 = 0

    #Poner aleatoreamente los barcos en tableros de los jugadores
    tablero_j1 = ["Transatlantico","Acorazado","Submarino",0,0,0,0,0,0,0]
    tablero_j2 = ["Transatlantico","Acorazado","Submarino",0,0,0,0,0,0,0]

    #shuffle (alterar el orden de los elementos de una lista aleatoriamente)
    random.shuffle(tablero_j1)
    random.shuffle(tablero_j2)

    #Jugamos tres rondas
    for i in range(3):
        print("Marcador jugador 1 -> " + str(marcador_j1) + " puntos")
        print("Marcador jugador 2 -> " + str(marcador_j2) + " puntos")
        for num_jugador in range(2):
            #El jugador dice una posición (0-9)
            posicion = int(input( jugadores[num_jugador] + " dime una posición entre 0-9"))


            #Saber que jugador está jugando y que tablero tiene que coger de referencia para hundir
            lista_referencia = []


            if num_jugador == 0:
                lista_referencia = tablero_j2
            else:
                lista_referencia = tablero_j1

            elemento_en_posicion = lista_referencia[posicion]

            puntos_en_ronda = 0
            if elemento_en_posicion != 0:
                if elemento_en_posicion == "Transatlantico":
                    print("Has hundido el Transatlantico")
                    puntos_en_ronda = 3
                elif elemento_en_posicion == "Acorazado":
                    print("Has hundido el Acorazado")
                    puntos_en_ronda = 4
                else:
                    print("Has hundido el Submarino")
                    puntos_en_ronda= 5
            else:
                print("AGUA")

            #Subimos los marcadores en funcion al jugador que esté jugando
            if num_jugador == 0:
                marcador_j1 += puntos_en_ronda
            else:
                marcador_j2 += puntos_en_ronda

            #Limpiar la posicion que ha dicho en el tablero
            if num_jugador == 0:
                tablero_j2[posicion]= 0
            else:
                tablero_j1[posicion]= 0


    #Decir cuantos puntos tiene cada jugador
    print("Jugador 1 has obtenido -> " + str(marcador_j1) + " puntos")
    print("Jugador 2 has obtenido -> " + str(marcador_j2) + " puntos")

    #Decir el ganador (puntuacion + alta)
    if marcador_j1 > marcador_j2:
        print("Ha ganado jugador 1!!")
    elif marcador_j2 > marcador_j1:
        print("Ha ganado jugador 2!!")
    else:
        print("EMPATE")

hundir_barcos()