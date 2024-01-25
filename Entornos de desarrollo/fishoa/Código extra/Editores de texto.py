"""
Este scrip es para tener códi extra para usar en lo exámenes de programación.
"""

#Para las personas que no ponen números enteros
def es_numero_entero (numero):

    try:  # con el try podemos comprobar si da error el código que le ponemos dentro
        int(numero)
        # Si no hay error, significa que lo que ha escrito es un número
        es_entero = True
    # Si hay un error, significa que lo que ha escrito no es un número
    except ValueError:
        es_entero = False

    return es_entero

#Poner nombre y apellido la primera en mayúsculas
def nombre_apellido (nombre):
    #primero separamos el nombre del apellido y los metemos en una lista
    nombre_lista = nombre.split()
    #creamos un texto para meter el nombre bueno
    nombre_bueno = ""
    #recorremos el nombre y el apellido
    for i in nombre_lista:
        nombre_bueno += i.capitalize() + " "
    return nombre_bueno

#