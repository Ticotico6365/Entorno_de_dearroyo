import random

def adivina_numero():

    #Pide el nombre al jugador
    nombre_jugador = input("Dime tu nombre:")

    #Elija un número entre el 1-10 -> numero secreo
    numero_secreto = random.randint(1,10)

    #Definimos el número de intentos
    intentos = 3


    #Al jugador que me diga números no superando 3 intentos
    while intentos > 0:
        #INTENTOS

        #1-> Pido número al jugador
        numero_dicho = input("Dime un número:")

        #Mientras el numero dicho no sea un int que lo pregunte de nuevo
        while not isinstance(numero_dicho, int):
            try:
                numero_dicho = int(input("Dime un número:"))
            except:
                print("No estás introduciendo un número!! Sé buena gente anda")


        #2 -> Comprobar si el número es el número secreto
        if numero_dicho == numero_secreto:
            #Si lo es
            # Se termina el juego (ACIERTA)
            print("FELICIDADES , HAS GANADO !!!")
            print("El número secreo es -> " + str(numero_dicho))
            print("Lo has acertado en " + str(4 - intentos) )
            intentos = -1

        else:
            #Si no lo es

            #Intentos -1
            intentos -= 1
            #Si el número es mayor
            if numero_secreto > numero_dicho:
                print("El número secreto es mayor que el tuyo")
            else:
                print("El número secreto es menor que el tuyo")
            #Seguir el juego

    if intentos == 0:
        print("HAS PERDIDO!!")
        print("El número secreto era: " + str(numero_secreto))






adivina_numero()
