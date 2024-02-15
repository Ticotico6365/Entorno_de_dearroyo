
def enlazar_listas (lista1,lista2): #ejercicio 3
    #creamos la lista final
    lista12 = []
    #hacemos un contador para ver el turno
    contador = 0
    #comprobamos si las listas tienen el mismo número de elementos
    if len(lista1) == len(lista2):
        #hacemos un bucle mientras que no se acaben las cosas para insertar
        while len(lista1) != 0 or len(lista2) != 0:
            contador += 1
            #como al contar 1es impar 2 es par 3 impar, y así sucesibamente, podemos hacerlo así
            if (contador%2 == 0):
                lista12.append(lista1[-1])
                lista1.pop(-1)
            else:
                lista12.append(lista2[-1])
                lista2.pop(-1)

    else:
        lista12 = []

    return lista12[::-1]

#print(enlazar_listas(["rojo","azul","amarillo"],["lunes","martes","miércoles"]))

def divide_lista (lista): #ejercicio 2
    #creamos los tipos de variable
    cadena = []
    entero = []
    floats = []
    bools = []
    #recorremos la lista
    for i in lista:
        #hacemos las comprobaciones pertinentes
        if isinstance(i,bool):
            bools.append(i)
        elif isinstance(i,int):
            entero.append(i)
        elif isinstance(i,float):
            floats.append(i)
        elif isinstance(i,str):
            cadena.append(i)

    #imprimimos los datos
    print("cadenas -> ", cadena)
    print("enteros -> ", entero)
    print("floats -> ", floats)
    print("bool -> ", bools)
#divide_lista(["fresa",2,"coco","piña",True,False,4.5,6,7,"Yo no sé",7.6,False])

lista = [{
    "nombre":"Ahri",
    "rol":"asesia",
    "tipo":["mago","movilidad"],
    "habilidades":{
        "Q":"orbe de ilusión",
        "W":"fascinación",
        "E":"encanto",
        "R":"impulso espiritual"
    }
},{
    "nombre":"Darius",
    "rol":"Luchador",
    "tipo":["Tanque","Daño Físico"],
    "habilidades":{
        "Q":"Hacha de Noxus",
        "W":"Golpe Cautelizador",
        "E":"Aprehesión",
        "R":"Guillotina Noxiana"
    }
},{
    "nombre":"Jinx",
    "rol":"Tiradora",
    "tipo":["Daño Físico"],
    "habilidades":{
        "Q":"Pow-Pow",
        "W":"Zap!",
        "E":"Lanzacohetes eléctricos",
        "R":"Supercohete de la muerte"
    }
},]

def roles_lista (lista): #ejercicio 6 A
    #creamos la lista con los roles de cada elemento
    roles = []
    #recorremos la lista
    for i in lista:
        roles.append(i["rol"])
    return roles

#print(roles_lista(lista))

def numero_tipo (lista): #ejercicio 6 B
    #creamos el sitio donde vamos a guardar la info
    tipo = {}
    #recorremos la lista
    for i in lista:
        tipo[i["nombre"]] = len(i["tipo"])
    return tipo
#print(numero_tipo(lista))

def busca_tipo (lista, tipo): #ejercicio 6 C
    #creamos una lista con los diccionarios que coinciden con los parametros desesdos
    nombre_tipo = []
    #~recorremos la lista
    for i in lista:
        if tipo in i["tipo"]:
            nombre_tipo.append(i)
    return nombre_tipo
#print(busca_tipo(lista,"Daño Físico"))

def lista_abilidades (lista): #ejercicio 6 D
    #creamos la variable donde va a estar la solución
    habilidades = []
    #recorremos la lista
    for i in lista:
        habilidades.append(i["habilidades"]["Q"])
        habilidades.append(i["habilidades"]["W"])
        habilidades.append(i["habilidades"]["E"])
        habilidades.append(i["habilidades"]["R"])
    habilidades.sort()

    return habilidades[::-1]
#print(lista_abilidades(lista))