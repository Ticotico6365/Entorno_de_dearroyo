import math


def di_nombre(): #ejercicio 1
    # Pedimos el nombre
    nombre = input("Escriba su nombre aquí:")

    return nombre
#print(di_nombre())

def pon_mayusculas(): #ejercicio 2
    # Pedimos el nombre
    nombre = input("Escriba su nombre aquí:")

    #lo pasamos a mayúsculas
    nombre = nombre.upper()

    return nombre
#print(pon_mayusculas())

def cuenta_letra(letra, palabra): #ejercicio 3
    #ponemos en la variable número el número de veces que aparece el caracter
    number = palabra.count(letra) #con el ".count" se ccuenta las veces que se repite algo

    return number

#print(cuenta_letra("a","Palabra"))

def invierte_palabra(palabra): #ejercicio 4
    #le damos la vuelta
    palabra = "".join(reversed(palabra))#con el .join insertamos en el vacío ("") la palabra dada la vuelta (reversed)
    """
    También se puede hacer así
    palabre = palabra [::-1] (este método es para listas, pero funciona porque phyton considera a una palabra una lista de caracteres)
    """
    return palabra
#print(invierte_palabra("HOla"))

def elimina_espacio(texto): #ejercicio 5
    #eliminamos espacio
    texto = texto.replace(" ", "") #con replace cambiamos los " "(espacios) por vacíos "".

    return texto
#print(elimina_espacio("Hola soy David"))

def text_sin_vocales (texto): #ejercicio 6

    #cogemos y sustuimos las vocales por vacios
    texto = texto.replace("a", "")
    texto = texto.replace("e", "")
    texto = texto.replace("i", "")
    texto = texto.replace("o", "")
    texto = texto.replace("u", "")

    return texto
#print(text_sin_vocales("Hola soy David"))

def text_contar_palabras(texto): #ejercicio 7
    """
    Si suponemos que el escritor es bueno y pone espacios bien, también se puede hacer así:
    texto = texto.count(" ") +1
    """
    texto = len(texto.split())

    return texto
#print(text_contar_palabras("Hola soy David"))

def palabra_palindroma (palabra): #ejercicio 8
    #damos la vuelta a la palabra igual que en el ejercicio 4
    palabra_reves = "".join(reversed(palabra))

    if palabra_reves == palabra:
        print("la palabra ",palabra, " es palíndroma")
    else:
        print("la palabra ",palabra, " no es palíndroma")

#palabra_palindroma("02022020")

def dos_letra_repetedida (text): #ejercicio 9
    #guardamos la letra primera
    letra_antes = ""
    #guardamos la palabra nueva
    palabra_nueva = ""
    #recorremos el texto
    for i in text:
        if i == letra_antes:
             palabra_nueva += "0"
        else:
            palabra_nueva += i
            letra_antes = i
    return palabra_nueva
#print(dos_letra_repetedida("Hooooooooola soooooooooooooooy   daaaaaaaaaaaaaaaaaavvvvvvvvvvvvvvvvvvvvvviiiiiiiiiiiiiiiiiiiifffffffffffffffffff"))

def quita_caracter_analfavetico(texto): #ejercicio 10
    """
    otro método:
    for i in texto:
        if i.isalpha() or i.isspace():  #isalpha comprueva todas las vocales y isspace comprueva los espacios.
            texto.replace(i,"")
    return texto
    """
    #ponemos todas los caracteres que queremos sustituir por lo que lo vamos a sustituir
    texto = texto.replace("1", "")
    texto = texto.replace("2", "")
    texto = texto.replace("3", "")
    texto = texto.replace("4", "")
    texto = texto.replace("5", "")
    texto = texto.replace("6", "")
    texto = texto.replace("7", "")
    texto = texto.replace("8", "")
    texto = texto.replace("9", "")
    texto = texto.replace("0", "")
    return texto
#print(quita_caracter_analfavetico("H1losfoi3243oiu425iu5b235b2iu3iu43"))

def palabra_larga(texto): #ejercicio 11
    #creamos variable vacia, donde vamos a almacenar la palara larga
    palabra_larga = ""
    #separamos las palabras del texto y las metemos en una lista
    texto = texto.split()
    #comparamos la palabra anterior con la siguiente para ver cual es más grande
    for i in texto:
        if len(i) >= len(texto):
            palabra_larga = i
    return palabra_larga
#print("la palabra más larga es: ",palabra_larga("hola cómo estas  estas david"))

def palabra_repetida(texto): #ejercicio 12
    #creamos una variable donde se guarden las palabras repetidas
    palabras_igual = []
    #separamos las palabras y las metemos en una lista
    texto = texto.split()
    #recorremos el texto insertando las palabras repetidas en una lista vacía.
    for i in texto:
        if texto.count(i) > 1:
            palabras_igual.append(i)
        while texto.count(i) > 1:
            texto.remove(i)
    print (palabras_igual)

#palabra_repetida("hola adiós hola pablo hola hola adiós pablo hola pipi pipi")

def orden_palabras (text): #ejercicio 13
    #separaos el texto
    lista_text = text.split()
    #la funcion sort ordena atomáticamente
    lista_text.sort()
    #juntamos lo anterior
    return " ".join(lista_text)

#print(orden_palabras("El apellido Bécquer o Bécker era y es bastante común en Alemania y Flandes. Proviene del oficio de panadero (en neerlandés bakker y en alemán bäcker). Hacia 1588 el católico Enrique Bécquer se trasladó con sus hijos Miguel y Adam desde la ciudad alemana de Moers, muy disputada durante la Guerra de los Ochenta Años, hasta Sevilla."))


def vocales_numeros (text): #ejercicio 14
    # ponemos todas los caracteres que queremos sustituir por lo que lo vamos a sustituir
    text = text.replace("a", "1")
    text = text.replace("e", "2")
    text = text.replace("i", "3")
    text = text.replace("o", "4")
    text = text.replace("u", "5")

    return text
#print (vocales_numeros("hola amigo soy tu primo aeiou dinosaurio"))

def enmascarada (text): #ejercicio 15

#En la corrección está más facil

    #creamos variable con la palabra inicial en lista
    text_fin = []
    #esto es un bucle que recorre las palabras
    for i in text.split():
        #metemos el contador dentro del bucle, para que se resetee por palabra
        contador = []
        #creamos otro bucle que recorra las letras de cada palabra
        for j in i:
            #insertamos en el contador las letras
            contador += j
            #comprovamos si las letras del contador son tan largas como el texto o es solo la primera
            if len(contador) == 1 or len(contador) == len(i):
                text_fin += j
            else:
                text_fin += "*"
    #combertimos la lista de texto a texto normal
    text_fin = "".join(map(str, text_fin))
    return text_fin
#print(enmascarada("Hola mundo"))

"""
Si solo nos pidiera una panabra:

def enmascara_palabra(palabra):
    
    #Tomamos las dos primeras letras de la palabra
    dos_primeras_letras = palabra[:2]
    #Tomamos las dos últimas letras de la palabra
    dos_ultimas_letras = palabra[-2:]
    
    #creamos una palabra final
    palabra = ""
    
    #Unimos las dos partes de la palabra en palabra final
    palabra_final += dos_primeras_letras + dos_ultimas_letras
    
print (enmascara_palabra("viernes"))
"""

def vuelta_text (text): #ejercicio 16
    #separamos las palabras
    text = text.split()
    #creamos variable para guardar la oración final
    text_fin = ""
    #creamos un bucle para que valla palabra por palabra
    for i in text:
        #metemos cada palabra dada la vuelta
       text_fin += "".join(reversed(i + " "))
    return text_fin
#print(vuelta_text("Hola mundo"))

def conta_digitos (text): #ejercicio 17
    # contador = text.count("1"+"2"+"3"+"4"+"5"+"6"+"7"+"8"+"9"+"0") Esto cuenta las veces que se repiten todos
    # return contador
    contador = 0
    # for i in text: Esto cuenta todos juntos
    #     if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
    #         contador = contador + 1
    # return contador

    contador1 = text.count("1")
    contador2 = text.count("2")
    contador3 = text.count("3")
    contador4 = text.count("4")
    contador5 = text.count("5")
    contador6 = text.count("6")
    contador7 = text.count("7")
    contador8 = text.count("7")
    contador9= text.count("8")
    contador0 = text.count("9")

    return "hay ",contador1, " unos", "hay ",contador2," doses", "hay ",contador3," treses", "hay ",contador4," cuatros", "hay ",contador5," cincos", "hay ",contador6," seises", "hay ",contador7," sietes","hay ",contador8," ochos", "hay ",contador9," nueves", "hay ",contador0," ceros"
#print(conta_digitos("1a2s3d4f5g6h7j8k9l0ñ1a2s3d4f5g6h7j8k9l0ñ"))

def conta_palabras_por_dig (text): #ejercicio 18
    #le preguntamos amablemente al usuario cuantos caracteres desea
    caracteres = input("cuánto quiere que mida la palabra que quiere contar: ")
    #creamos el contador, donde se va a guardar el número de palabras
    contador = 0

    text = text.split()

    for i in text:
        if len(i) == caracteres:
            contador += 1
    return contador
#print(conta_palabras_por_dig("Hola mundo, soy david y estoy aquí"))

def vuelta_texto (text): #ejercicio 19
    #creamos lista del texto
    lista_texto = text.split()
    #le damos la vuelta a los elementos de la lista
    lista_texto = lista_texto [::-1]
    #combertimos la lista en texto
    text = " ".join(lista_texto)
    return text
#print(vuelta_texto("Hola mundo"))

def sin_consonan (text): #ejercicio 20
    text_fin = []
    #recorremos la palabras
    for i in text:
        #Comprovamos si cada letra es una consonante o vocal
        if not(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):  #isalpha comprueva todas las vocales y isspace comprueva los espacios.
            text_fin += i
    return "".join(map(str, text_fin))
#print(sin_consonan("Hola mundo soy david"))

def capitaliza (text): #ejercicio 21
    """
    esto es una solución directa, ya que title ya te pone las palabras en mayúscula
    return texto.lower().title()
    """
    #separamos el texto
    text = text.lower().split()
    #creamos una lista con las palabras con la primera en mayúsculas
    text_fin = []
    #vamos palabra por palabra poniendo la primera en mayúsculas
    for i in text:
        text_fin.append(i.capitalize())

    return " ".join(text_fin)
#print(capitaliza("hola mundo soy david"))

def cuenta_letra (text): #ejercicio 22
    #preguntamos la letra
    contador = input("Qué letra le gustaría contar: ")
    #contamos las letras
    text = text.count(contador)
    return "hay " + str(text)
#print(cuenta_letra("Nacido según algunos autores en la ciudad de Itálica (un municipium de la Hispania Baetica), la gens de Trajano sería de origen itálico y, posiblemente, también turdetano."))

def eliminar_repe (text): #ejercicio 23
    #texto donde se va a recoger el texto final
    text_fin = ""
    #recorremos las letras del texto
    for i in text:
        #si la letra no está en el texto final y no es un espacio, lo añado a texto final
        if i not in text_fin or i == " ":
            text_fin += i
    return text_fin
#print(eliminar_repe("Existen dos tesis sobre el origen del emperador Trajano, según la primera nació en la ciudad romana de Itálica (actual Santiponce), adscrita a la provincia de la Bética, una de las más intensamente romanizadas del Imperio, el 18 de septiembre del año 53."))

def palara_por_asterisco (text): #ejercico 25
    #creamos la variable con el número de letras de la palabra que queremos cambiar
    numero = 4
    #separamos el texto en palabras
    text = text.split()
    #guardamos la frase en una variable vacía
    text_fin = ""
    #recorremos las palabras para ver cual es delnúmero especificado de letras
    for i in text:
        if len(i) >= numero:
            text_fin += "*" * len(i) + " "
        else:
            text_fin += i + " "

    return text_fin
#print(palara_por_asterisco("Hola soy David y tengo cuat ro letras 1234"))

def conatdor_de_palabra (texto, palabra):
    #pasar todos a minúscula
    texto = texto.lower()
    palabra = palabra.lower()
    texto = texto.split()
    contador = 0
    for i in texto:
        if palabra in texto:
            contador += 1
    return contador
#print(conatdor_de_palabra("Hola que ase", "que"))

def sin_espacio_fin (text): # ejericio 27
    return text.strip()
#print(sin_espacio_fin("                                HOla                                                                      "))

def pares_es_X (text): #ejercicio 28
    #creamos lista donde se va a guardar el texto final
    text_fin = []
    #conatmos por cual número nde la cadena va
    contador = 1
    #separamos el texto en una lista de palabras
    text = text.split()
    #recorremos la lista de palabras
    for i in text:
        #por cada palabra insertamos un espacio
        text_fin += " "
        #recorremos las letras de cada palabra
        for j in i:
            #contamos el número de letras de la palabra
            contador += 1
            #comprovamos si el número es par o impar
            if ((contador/2) - math.trunc(contador/2)) != 0: # el porcentage es el módulo % se podría haber hecho así (i%2 == 0)
                text_fin += "X"
            else:
                text_fin += j
    return "".join(text_fin)

#print(pares_es_X("Hola ke ase"))

"""
ejemplo del condicional anterior ( if ((contador/2) - math.trunc(contador/2)) != 0: ):
    -si el contador = 3:
     3/2 = 1,5
     si lo truncamos (math.trunc) sería 1
     1,5 - 1 = -0.5
     como es diferente de 0 es número es impar
    -si el contador = 4
     4/2 = 2
     si lo truncamos (math.trunc) quedaría igual (2)
     2 - 2 = 0 
     por lo tanto el número es par
"""

def cifrado_cesar (text): #ejercicio 29
    #ponemos el texto en minuscula para que las letras estén en nuestra lista
    text = text.lower()
    #creamos una lista con todas las letras en minúsculas
    abcdario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a"]
    #contamos la posición de las letras en la lista
    indice_letra = 0
    #creamos una lista vacía para meter el texto final
    text_fin = ""
    #recorremos letra por letra
    for i in text:
        #si no pertenece a la lista donde está el abcdario, se deja igual
        if i not in abcdario:
            text_fin += i
        #si pertenece a esa lista se cambia por la siguiente
        else:
            indice_letra = abcdario.index(i) #toamamos el índice de la letra en la lista
            text_fin += abcdario[indice_letra + 1] #le sumamos 1 para que ponga la siguiente

    return text_fin
#print(cifrado_cesar("Hola mundo, soy David"))