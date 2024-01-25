
def bucle_normal ():
    for i in range(5):
        if i == 0:
            print("me he ejecutado: " + str(i +1) + " vez")
        else:
            print("me he ejecutado: " + str(i +1) + " veces")

#bucle_normal()

def bucle_raro (palabra):

    for i in palabra:
        print(i)

#bucle_raro("Hipopotomostrosesquipedaliofovia")

def poner_consonantes (palabra):
    for i in palabra:
        if not (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
            print(i)

#poner_consonantes("Hipopotomostrosesquipedaliofovia")


def bucle_while (contador):
    while contador > 0:
        contador -= 1
        print("Hola")

bucle_while(10)