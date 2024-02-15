import random
import time

# print(random.randint(1,100))

def genera_carton():
    #hago una variable con una lista vacia
    lista_numeros = []

    #Bucle while, mientras la lista no tenga 9 números
    while len(lista_numeros) != 9:

        #genero un número aleatorio
        num_aleatorio = random.randint(1,99)

        #Compruebo que ese número no esté en la lista
        if num_aleatorio not in lista_numeros:
            #Metemos el número en la lista
            lista_numeros.append(num_aleatorio)

        #Ordenamos los números
        lista_numeros.sort()

    return [lista_numeros[:3], lista_numeros[3:6], lista_numeros[6:]]





def dime_numero(lista_numeros_dichos):

    #Generamos un número aleatorio
    num = random.randint(0,99)

    #mientras el número esté en la lista
    while num in lista_numeros_dichos:
        #Lo genere de nuevo
        num = random.randint(0, 99)

    return num



def comprueba_linea(lista_numeros_dichos, carton):

    linea_1_completa = False
    linea_2_completa = False
    linea_3_completa = False

    for numero in carton[0]:
        if numero in lista_numeros_dichos:
            linea_1_completa = True
        else:
            linea_1_completa = False
            break
    for numero in carton[1]:
        if numero in lista_numeros_dichos:
            linea_2_completa = True
        else:
            linea_2_completa = False
            break
    for numero in carton[2]:
        if numero in lista_numeros_dichos:
            linea_3_completa = True
        else:
            linea_3_completa = False
            break

    return linea_1_completa or linea_2_completa or linea_3_completa



def comprueba_bingo(lista_numeros_dichos, carton):
    contador_linea_1 = 0
    contador_linea_2 = 0
    contador_linea_3 = 0

    for numero in carton[0]:
        if numero in lista_numeros_dichos:
            contador_linea_1 +=1

    for numero in carton[1]:
        if numero in lista_numeros_dichos:
            contador_linea_2 +=1

    for numero in carton[2]:
        if numero in lista_numeros_dichos:
            contador_linea_3 +=1

    if contador_linea_1 ==3 and contador_linea_2 ==3 and contador_linea_3 ==3:
        return True
    else:
        return False


def comprueba_linea_break(lista_numeros_dicho, carton):

    linea_completa = False

    for linea in carton:
        for numero in linea:
            if numero in lista_numeros_dicho:
                linea_completa = True
            else:
                linea_completa = False
                break
        if linea_completa:
            break

    return linea_completa

def comprueba_fin_juego(lista_numeros_dichos, cartones, num_jugadores):
    hay_bingo = False
    for i in range(num_jugadores):
        tiene_bingo = comprueba_bingo(lista_numeros_dichos, cartones[i])
        if tiene_bingo:
            hay_bingo = True
            break

    return hay_bingo


def el_bingo():

    #Lista números dichos
    lista_numeros_dichos = []
    hay_linea = False

    #Preguntar cuantos jugadores
    num_jugadores = int(input("Dime cuantos jugadores sois:"))

    #generamos cartones
    cartones = []
    for i in range(num_jugadores):
        carton = genera_carton()
        cartones.append(carton)

    while not comprueba_fin_juego(lista_numeros_dichos, cartones, num_jugadores):

        #Sacamos numero
        numero_nuevo = dime_numero(lista_numeros_dichos)
        print("NUEVO NÚMERO --> " + str(numero_nuevo))
        time.sleep(0.5)

        #Metemos el número dentro de los números dichos
        lista_numeros_dichos.append(numero_nuevo)
        lista_numeros_dichos.sort()
        print("LISTA NÚMEROS -->" + str(lista_numeros_dichos))
        time.sleep(0.5)

        #Comprobar lineas
        if len(lista_numeros_dichos) >= 3 and hay_linea == False:
            for i in range(num_jugadores):
                if comprueba_linea(lista_numeros_dichos, cartones[i]):
                    print("El jugador" + str(i) + "ha conseguido linea!!")
                    hay_linea = True
                    print(cartones[i])
                    time.sleep(5)
                    break

        # Comprobar Bingo
        if len(lista_numeros_dichos) >= 9:
            for i in range(num_jugadores):
                if comprueba_bingo(lista_numeros_dichos, cartones[i]):
                    print("El jugador" + str(i) + "ha conseguido bingo!!")
                    print("FIN DEL JUEGO")
                    print(cartones[i])
                    break



el_bingo()