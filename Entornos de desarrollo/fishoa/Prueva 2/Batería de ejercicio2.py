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

print(sustituye_vocales_por_numeros("murciegalo"))

def cambio_letra (letra1, letra2):
