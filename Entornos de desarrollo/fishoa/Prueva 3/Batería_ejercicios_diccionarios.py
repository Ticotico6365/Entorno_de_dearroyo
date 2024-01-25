# Paso 1: Crear un diccionario de juguetes
juguetes = {
    "a":1,
    "pelota": 10,
    "muñeca": 15,
    "coche": 20,
    "rompecabezas": 18,
    "peluche": 12,
    "robot": 25,
    "pistola de agua": 8,
    "tren de juguete": 22,
    "oso de peluche": 14,
    "cometa": 10,
    "bloques de construcción": 30,
    "balón de fútbol": 16,
    "patineta": 35,
    "avión de juguete": 24,
    "casa de muñecas": 28
}
separacion = "_"  # la he creado para separar, no es un ejercicio.


print(separacion.center(100, "_"))
print("ejercicio 2")
#Ejercicio 2: Acceder a un valor en el diccionario
jugete_buscar = input("De que juguete desea de mirar el precio: ")
print(juguetes[jugete_buscar], "€")

print(separacion.center(100, "_"))
print("ejercicio 3")
#Ejercicio 3: Modificar un valor en el diccionario
jugete_modificar_precio = input("De que jugete desea modificar el precio: ")

valor_nuevo = input("Cuámto desea que cueste: ")
print("el jugete",juguetes[jugete_modificar_precio],"ahora costará",valor_nuevo,"€")

print(separacion.center(100, "_"))
print("ejercicio 4")
#Ejercicio 4: Agregar un nuevo juguete al diccionario
jugete_nuevo = input("Inserte el nombre del nuevo juguete: ")
precio_nuevo = input("Cuámto desea que cueste: ")
juguetes[jugete_nuevo] = precio_nuevo
print(juguetes)

print(separacion.center(100, "_"))
print("ejercicio 5")
#Ejercicio 5: Recorrer el diccionario de juguetes
lista_precios = []
lista_jugetes = []
for i in juguetes:
    lista_jugetes.append(i)
    lista_precios.append(str(juguetes[i]))
    print("el jugete", lista_jugetes[-1], "vale", lista_precios[-1], "€")

print(separacion.center(100, "_"))
print("ejercicio 6")
#Ejercicio 6: Calcular el precio promedio de los juguetes

sumador_precio = 0
for j in juguetes.values():
    sumador_precio += j

media = round(sumador_precio/len(juguetes))
print(media)

print(separacion.center(100, "_"))
print("ejercicio 7")