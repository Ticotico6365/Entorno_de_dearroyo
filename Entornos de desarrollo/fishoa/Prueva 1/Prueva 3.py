"""""
Los ejercicios están separados por una barra.
"""""
separacion = "_"  # la he creado para separar, no es un ejercicio.


def Ejercicio_1 ():

    """""
    Pedimos el nombre del usuario por consola (el input hace que el progarma espere a que reponda el usuario).
    """""
    nombre_usuario = input("Escribe tu nombre aquí:")

    #Imprimimos por consola lo que nos escribe el usuario
    return nombre_usuario

print(ejercicio_1())


print(separacion.center(100, "_"))

def pide_tu_nombre_y_pon_mayusculas ():

    #pedimos nombre de usuario
    nombre_usuario = input("Tu nombre, por favor")

    #poner el nombre ne maysucualas
    nombre_usuario_mayuscula = nombre_usuario.upper()

    return nombre_usuario_mayuscula

print(pide_tu_nombre_y_pon_mayusculas())


print(separacion.center(100, "_"))