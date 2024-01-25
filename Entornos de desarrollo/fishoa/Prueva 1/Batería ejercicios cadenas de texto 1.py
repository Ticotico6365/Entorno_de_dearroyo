"""""
Los ejercicios están separados por una barra horizontal.
"""""
separacion = "_"  # la he creado para separar, no es un ejercicio.


def ejercicio_1 ():

    #Pedimos el nombre
    nombre = input("Escriba su nombre aquí:")

    return nombre
print(ejercicio_1())

print(separacion.center(100, "_"))

def ejercicio_2 ():

    #Pedimos el texto
    texto = input("Escribe el texto aquí:")

    #Lo pasamos a mayúsculas
    texto_mayuscula =  texto.upper()

    return texto_mayuscula
print(ejercicio_2())

print(separacion.center(100, "_"))

def ejercicio_3 ():

    #Pedimos texto
    texto = input("Escriba su texti aquí:")

    #conatmos la letra "a"
    texto_contar = texto.count("a")

    return texto_contar

print(ejercicio_3())

print(separacion.center(100, "_"))

def ejercicio_4():

    #Pedimos texto
    texto = input("Ponga su texto aquí para ser volteado:")

    #le damos la vuelta

    texto_vuelta = texto[::-1]

    return texto_vuelta
print (ejercicio_4())

print(separacion.center(100, "_"))
def ejercicio_5():

    #Pedimos texto
    texto = input("Ponga su texto con espacio aquí")

    #definimos lo que buscamos y por lo que lo queremos sustituir
    buscar = " "
    cambiar_por = ""

    #hacemos que cambie lo que buscamos por lo que cambiamos
    texto_noespacio = texto.replace(buscar, cambiar_por)

    return texto_noespacio

print(ejercicio_5())

print(separacion.center(100, "_"))

def ejercicio_6():

    #Pedimos texto
    texto = input("Pon texto:")

    #definimos lo que buscamos y por lo que lo queremos sustituir
    cambiar_por = ""
    vocales = list[a,e,i,o,u]
    # hacemos que cambie lo que buscamos por lo que cambiamos
    texto_novocal = texto.replace(vocales, cambiar_por)

    return texto_novocal
print(ejercicio_6())


