def esPar (numero):
    return numero%3 == 0

def sumatoriaDijitos (numero):
    total = 0
    while total ==0:
        ultimDijito = numero%10
        total = total + ultimDijito
        numero = numero // 10
    return total

cantidadImpares = 0
n = int(input("Escribe un número: "))
while sumatoriaDijitos(n) < 1000 and sumatoriaDijitos(n) %3 !=0:
    if esPar(n):
        cantidadImpares = cantidadImpares + 1
        n = int(input("Escribe un número: "))

print("Cntidad de impares: ",cantidadImpares)
"""
1.- Al ejecutar el código sin ninguna modificación observamos que no nos vuelve a preguntar el nuevo número, pero como cuando meto un número impar no me lo cuenta, sospecho que no cuenta los números impares.

2.- Ponemos el punto del ruptura en la línea 14 y vamos dandole al step into, para que nos valla dirigiendo a los métodos:
    2.1.- nos fijamos que en el método sumatoriaDijitos no se mete en ell while, y me fijo que es debido a que efectivamente el while solo se ejecutará si el total es diferente de 0, pero
"""


















# def viaje ():
#     #1.- pedimos por consola la duración del viage en minutos sabiendo que nos va a dar un úmero entero
#     duracion_minutos = int(input("Por favor, introduzca la duración de su viaje en minutos, si es tan amable: "))
#     #2.- calculamos el coste del viaje
#     #3.- imprimimos los resultados
#     print("si su viaje es de",duracion_minutos,"minutos:")
#     print("si ha hecho su viaje con Acciona y modo standart, su vaije saldrá por: ",0.31 * duracion_minutos,"€")
#     print("si ha hecho su viaje con Acciona y modo Custom, su vaije saldrá por: ", 0.36 * duracion_minutos,"€")
#     print("si ha hecho su viaje con Acciona y modo X-tra, su vaije saldrá por: ", 0.39 * duracion_minutos,"€")
#
# #viaje()




# def max (n1, n2):
#     if n2 < n1:
#         """
#         Al darle por primera vez al debug poniendo el punto de ruptura en la línea 2, me doy cuenta que lo primero que hace es comprobar si 50 es menor que 100, y como es cierto nos devuelve 100, esto está mal, debido a que nos debe de dar el número mayor. Por lo tato ponemos que debuelva n1
#         """
#         return n1 #return n2
#     #elif n1 < n2:
#     # """
#     # Si cambiamos los números de sitio y ponemos que n2 = 100 y n1 = 50,vemos que como el elif se cumple y pues como en el anterior if, nos debueve el malo, por lo tanto si nos fijamos, despues del else, está bien, por lo tanto podemos borrar la parte del elif.
#     # """
#         #return n1
#     else:
#         return n2
#
# print(max(100, 50))