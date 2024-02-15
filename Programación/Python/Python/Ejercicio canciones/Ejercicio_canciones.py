#INsertamos la lista de canciones
from lista_canciones import lista_canciones

def pintar_nombre_autor_duracion (lista_canciones): #ejercicio 1

    #recorremos la lista de canciones
    for i in lista_canciones:

        print(i["nombre"],"//",i["autor"],"->",i["duracion"])

#pintar_nombre_autor_duracion(lista_canciones)

def devuelve_nombre_canciones (lista_canciones): #ejercicio 2
    #guardamos los nombres de las canciones
    nombre_canciones = []
    #recorremos la lista de canciones
    for i in lista_canciones:
        nombre_canciones.append(i["nombre"])

    return nombre_canciones

#print(devuelve_nombre_canciones(lista_canciones))

def suma_duracion_canciones (lista_canciones): #ejercicio 3
    #guardamos la suma
    suma_total = 0
    #recorremos la lista de canciones
    for i in lista_canciones:
        #para poder sumar los minutos y segundos de una canción primero separamos la duración por los ":"
        duracion_separada = i["duracion"].split(":")
        #sumamos los minutos pasados a segundos y los segundos los dejamos igual
        suma_total += int(duracion_separada[0])*60 + int(duracion_separada[1])

    return suma_total
#print(suma_duracion_canciones(lista_canciones))

def canciones_con_videopclip (lista_canciones): #ejercicio 4
    #creamos la lista donde se guardarán las canciones con videoclip
    canciones_videoclip = []
    #recorremos las canciones
    for i in lista_canciones:
        if i["tiene_videoclip"]:
            canciones_videoclip.append(i)

    return canciones_videoclip
#print(canciones_con_videopclip(lista_canciones))

def cancion_por_anyo (lista_canciones, anyo): #ejercicio 5
    #guardamos canciones dentro del rango
    canciones_anyo = []
    #recorremos las canciones
    for i in lista_canciones:
        #comprobamos si conciden los años
        if anyo == i["anyo"]:
            canciones_anyo.append(i)

    return canciones_anyo
#print(cancion_por_anyo(lista_canciones, 2013))

def cancion_por_cadena_texto (lista_canciones, text): #ejercico 6
    #guardamos la cancion
    canciones = []
    #recorremos las canciones
    for i in lista_canciones:
        #comprobamos si el texto coincide
        if i["nombre"].lower().count(text.lower()) > 0 or i["autor"].lower().count(text.lower()) or i["disco"].lower().count(text.lower()):
            canciones.append(i)

    return canciones
#print(cancion_por_cadena_texto(lista_canciones,"VIDA"))

# def intervalo_anyo (lista_canciones,anyo1,anyo2): #ejercicio 7
#     #guardamos canciones
#     canciones = []
#     canciones_arriba = []
#     canciones_abajo = []
#     #recorremos las canciones
#     for i in lista_canciones:
#         if i["anyo"] > anyo1:
#             canciones_arriba.append(i)
#         elif i["anyo"] < anyo1:
#             canciones_abajo.append(i)
#         elif i["anyo"] > anyo2:
#             canciones_arriba.append(i)
#         elif i["anyo"] < anyo2:
#             canciones_abajo.append(i)
#     return canciones
# print(intervalo_anyo(lista_canciones,2013,2022))

def cuanto_genero (lista_canciones, genero):
    #guardamos el número
    num_canciones = 0
    #recoremos canciones
    for i in lista_canciones:
        if