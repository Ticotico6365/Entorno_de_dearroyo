#Creación y Acceso a Listas
def alumnos_clase (): #ejercicio 1
    alumnos = ["Alba", "Alberto", "Luis", "Rodrigo"]
    print(alumnos[1])

    nuevo_alumno = input("el alumno nuevo se llama: ")
    alumnos += nuevo_alumno.split()
    print(alumnos)

#alumnos_clase()

#Modificación de Listas
def ejercicio_2 ():
    numeros  = [1,2,3,4,5,6,7,8,9,0]

    numeros.insert(numeros.index(3), 10)
    numeros.remove(3)
    numeros.pop(-1)
    print(numeros)
ejercicio_2()

#Bucles y Listas
def ejercicio_3 ():

    numeros = [1,2,3,4,5,6,7,8,9,10]

    for i in numeros:
        print(i)
#ejercicio_3()

#Filtrado de Listas
def ejercicio_4 ():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    par = []
    for i in numeros:
        if i%2 == 0:
            par.append(i)
    print(par)
#ejercicio_4()

#Suma de Listas
def ejercicio_5 ():
    numeros = [1, 2, 3, 4, 5]
    suma = 0
    for i in numeros:
        suma = i + suma
    print (suma)
#ejercicio_5()

# Matrices y Listas Anidadas
def ejercicio_6 ():
    matriz = [[1,0,0],[0,1,0],[0,0,1]]
    suma = 0
    for i in matriz:
        print(i)
        for j in i:
            suma = j +suma
    print("la suma es", suma)
#ejercicio_6()

#Listas y Funciones
def ejercicio_7 ():
    promedio_lista = [1,2,3,4,5,6,7,8,9]
    suma = 0
    for i in promedio_lista:
        suma = i + suma
    print (suma/len(promedio_lista))

#ejercicio_7()

#Listas y Condicionales
def ejercicio_8 ():
    mates = [1,2,3,4,5,6,7,8,9]
    for i in mates:
        if i >= 5:
            print("ha aprovado con un ", i)
        else:
            print("ha suspendido con un ", i)
#ejercicio_8()

#Listas y Ordenamiento
def ejercicio_9():
    nombres_desordenados = ["Albero","Indira", "Pablo", "Andrea", "Silvia", "Zapatero"]
    nombres_desordenados.sort()
    print(nombres_desordenados)
#ejercicio_9()

def ejercicio_10 ():
    lista = ["pito", "wonder", "hipopotomostrosesquipedaliofóvia", "xilófono", "iluso"]
    busqueda = input("ingrese la palabra que desea buscar: ")
    if lista == busqueda:
        print("se ha encontrado lo que buscaba")
    else:
        print("no se ha encontrado lo que buscaba")
#ejercicio_10()

def ahocado ():
    palabr_oculta = []