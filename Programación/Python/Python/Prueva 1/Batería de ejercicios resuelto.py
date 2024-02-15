def pon_mayusculas (palabra): #ejercicio 2.

    #pongo la palabra que me manda en mayúsculas.
    palabra_mayuscula = palabra.upper()

    #imprime la palabra en mayúscualas.
    print(palabra_mayuscula)

#pon_mayusculas("pedro")

def cuenta_aes (palabra): #ejercicio 3

    #Pasamos la palabra a mayuscula.
    palabra = palabra.upper()

    #contamos las aes qie hay dentro de la palabra
    contador_A = palabra.count("A")

    return contador_A

#print(cuenta_aes("pasapalabra"))

def invierte_palabra (palabra): #ejercicio 4

    #creamos una palabra vacía ("") y unimos la palbra que nos pase al revés (reverse)
    palabra_invertida = "".join(reversed(palabra))

    return palabra_invertida

#print(invierte_palabra("Hola"))

def elimina_espacio (texto): #ejercicio 5

    #quitamos los espacios
    texto = texto.replace(" ","")

    return texto
print(elimina_espacio("este finde me voy de copas"))

def elimina_vocales(texto): #ejercicio 6

    texto = texto.replace("a","")
    texto = texto.replace("e", "")
    texto = texto.replace("i", "")
    texto = texto.replace("o", "")
    texto = texto.replace("u", "")

    return texto

#print(elimina_vocales(abcdario))

def conatar_palabras(texto):

    #contador_espacios = texto.count(" ") + 1
    #return contador_espacios
    lista_palabras = texto.split()
    return len(lista_palabras)

print(conatar_palabras("Hoy es viernes"))