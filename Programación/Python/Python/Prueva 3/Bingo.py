import random
def generar_carton ():
    #creamos el catón como lista única
    carton = []
    #mientras que no haya nueve números se repite la operación
    while len(carton) != 9:
        #generamos el número aleatorio
        numero_aleatorio = random.randint(1, 99)
        #si no se repite se mete en la lista
        if numero_aleatorio not in carton:
            carton.append(numero_aleatorio)
    return [carton[:3], carton[3:6], carton[6:]]

def dime_numero (ya_salido):
    #generamos un número aleatorio
    num_nuevo = random.randint(0,99)
    #mientras el número esté en la lista que valla generando números
    while num_nuevo in ya_salido:
        num_nuevo = random.randint(0, 99)

    return num_nuevo

def victoria_linea (lista, carton):
    victory = False
    for line in carton:
        for numero in line:
            if numero in lista:
                victory = True
            else:
                victory = False
                break #para el proceso
        if victory == True:
            return victory

def comprueva_fin(lista_num, cartones, num_jugadores):
    hay_bingo = False
    for i in range(num_jugadores):
        tiene_bingo = comprueba_bingo()

def el_bingo ():
    Lista_de_números_dichos = []
    num_jugadores = int (input("Dime el número de jugadores"))
    cartones = []
    for i in range (num_jugadores):
        carton = generar_carton()
        cartones.append(carton)
    while