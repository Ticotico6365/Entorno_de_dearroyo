"""""
Los ejercicios están separados por una barra horizontal.
"""""
separacion = "_"  # la he creado para separar, no es un ejercicio.


def ejercicio_1 ():

    #Pedimos el nombre
    nombre = input("Escriba su nombre aquí:")

    return nombre
#print(ejercicio_1())

print(separacion.center(100, "_"))

def ejercicio_2 ():

    #Pedimos el texto
    texto = input("Escribe el texto aquí:")

    #Lo pasamos a mayúsculas
    texto_mayuscula =  texto.upper()

    return texto_mayuscula
#print(ejercicio_2())

print(separacion.center(100, "_"))

def ejercicio_3 ():

    #Pedimos texto
    texto = input("Escriba su texti aquí:")

    #conatmos la letra "a"
    texto_contar = texto.count("a")

    return texto_contar

#print(ejercicio_3())

print(separacion.center(100, "_"))

def ejercicio_4():

    #Pedimos texto
    texto = input("Ponga su texto aquí para ser volteado:")

    #le damos la vuelta

    texto_vuelta = texto[::-1]

    return texto_vuelta
#print (ejercicio_4())

print(separacion.center(100, "_"))
def ejercicio_5():

    #Pedimos texto
    texto = input("Ponga su texto con espacio aquí")

    #definimos lo que buscamos y por lo que lo queremos sustituir
    buscar = " "
    cambiar_por = ""

    #hacemos que cambie lo que buscamos por lo que cambiamos
    texto_noespacio = texto.replace(buscar, cambiar_por)

    return texto_noespacio

#print(ejercicio_5())

print(separacion.center(100, "_"))

def ejercicio_6():

    #Pedimos texto
    texto = input("Pon texto:")

    #definimos lo que buscamos y por lo que lo queremos sustituir
    cambiar_por = ""
    vocales = list[a,e,i,o,u]
    # hacemos que cambie lo que buscamos por lo que cambiamos
    texto_novocal = texto.replace(vocales, cambiar_por)

    return texto_novocal
#print(ejercicio_6())

#Ejercicio 8
def es_palindromo(texto):
    #definimos una variable con el texto normal (texto1) y otra con el texto volteado (texto2)
    texto1 = texto
    texto2 ="".join(reversed(texto))
    if texto1 == texto2:
        print("la palabra",texto1,"es palíndroma")
    else:
        print("la palabra", texto1, "no es palíndroma")

#es_palindromo("02022020")

def eliminador_noalfabetico(texto): #ejercicio 10
    listanum = [1,2,3,4,5,6,7,8,9,0]
    #separamos lo alfabetico por lo anafabetico
    texto_todo = texto.split("1","2","3","4","5","6","7","8","9","0")

    texto_fin += texto.replace(texto_todo,"")

    print(texto_fin)
#eliminador_noalfabetico("12lola flor4324es ")

#ejercicio 12
def cuenta_palabra_en_texto(texto,palabra):

    return texto.count(palabra)

#print(cuenta_palabra_en_texto("El origen de la relación de esta especie con el ser humano se remonta al Neolítico, y concretamente en el marco del cambio de sociedades cazadoras-recolectoras a agricultoras-ganaderas. Algunos estudios revelan que las primeras gallinas y pollos domesticados pueden provenir de la India, hace más de 4000 años. Su presencia en la vida del hombre no es nueva. Los primeros restos datan del Neolítico, del año 6000 a. C. Fueron encontrados en la provincia china de Hebei y de ahí pasaron a Europa de la mano de los sumerios. En el Egipto de Tutmosis III (1500 a. C.) ya hay constancia de avicultores, y en los tratados gastronómicos de la Roma del siglo i d. C. Los avances de la ciencia, así como los nuevos conocimientos higiénicos-sanitarios, permitieron la extensión del consumo de pollo a toda la población durante el siglo xx. Su década prodigiosa llegó en 1960. Dejó de ser un artículo de lujo para convertirse en un producto habitual en las dietas debido a su alto contenido proteico y vitamínico y la muy baja presencia de grasas.", "-"))

def sustituye_vocales_por_numeros (palabra): #ejercicio 14 sin bucle
    palabra = palabra.replace ("a", "1")
    palabra = palabra.replace("e", "2")
    palabra = palabra.replace("i", "3")
    palabra = palabra.replace("o", "4")
    palabra = palabra.replace("u", "5")

    return palabra

#print(sustituye_vocales_por_numeros("murciegalo"))

def change_alfabet (word, letra1, letra2): #ejercicio 9 mal

        word = word.replace(letra2, letra1)
        return word
#print(change_alfabet("lana","b","a"))

def dos_letra_repetedida (text): #ejercicio 9 bien
    letra_antes = ""
    palabra_nueva = ""
    for i in text:
        if i == letra_antes:
             palabra_nueva += "0"
        else:
            palabra_nueva += i
            letra_antes = i
    return palabra_nueva
#print(dos_letra_repetedida("dabale aaroz aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaauaaaaaaaaaaaaaaaaaaaa la aaaruga                                            eirpw fseifjsiiieei"))


def longuest_word (text):#ejercicio11
    palabra_larga = ""
    text = text.split()
    for  i in text:
        if len(i) > len(text):
            palabra_larga += i
    return palabra_larga
#print(longuest_word("hola cómo esta"))

def ordena_alfabet (text):
    palabras = text.split()
    palabras = palab