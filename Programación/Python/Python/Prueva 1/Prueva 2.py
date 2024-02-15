"""""
Los ejercicios están separados por una barra.
"""""
separacion = "_"  # la he creado para separar, no es un ejercicio.


def pedir_nombre ():

    """""
    Pedimos el nombre del usuario por consola (el input hace que el progarma espere a que reponda el usuario).
    """""
    nombre_usuario = input("Escribe tu nombre aquí:")

    #Imprimimos por consola lo que nos escribe el usuario
    return nombre_usuario

print(separacion.center(100, "_"))

def pide_tu_nombre_y_pon_mayusculas ():

    #poner el nombre ne maysucualas
    nombre_usuario_mayuscula = pedir_nombre().upper()

    return nombre_usuario_mayuscula

print(pide_tu_nombre_y_pon_mayusculas())


print(separacion.center(100, "_"))