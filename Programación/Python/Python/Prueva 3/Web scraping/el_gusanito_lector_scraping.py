import requests
import bs4

libreria = {
    "portada": "",
    "nombre": "",
    "autor": "",
    "precio": 0.00,
    "descrippcion": "",
    "ISBN": ""
}
def es_numero_entero (numero): #creamos un método para la gente que mete números en vez de palabras
    # creamos una variable que guarde el número que dice el jugador

    es_entero = False #variable que dice si es verdad que es entero

    try:  # con el try podemos comprobar si da error el código que le ponemos dentro
        int(numero)
        # Si no hay error, significa que lo que ha escrito el jugador es un número
        es_entero = True
    # Si hay un error, significa que lo que ha escrito el jugador no es un número
    except ValueError:
        es_entero = False

    return es_entero

def es_un_ISBN(isbn):#creamos un método que comprueba si es un isbm

    isbn = isbn.replace("-","") #le quitamos lo que no queremos, poniéndolo en el formato deseado
    #todos los isbn tiernen 13 caracteres y son númericos
    if len(isbn) == 13 and es_numero_entero(isbn) == True:
        return True
    else:
        return False
es_un_ISBN("pepe")
def obtener_conrtenido_pagina_web(url):

    #hacemos petición a la url de la página web para obtener su HTML
    pagina_html = requests.get(url)

    #Analizamos el HTML obtenido con bs4
    soup = bs4.BeautifulSoup(pagina_html.content, "html.parser")

    #Devolvemos la sopa de bs4
    return soup

def extracxion_de_datos():

    todos_libros = []

    #recorremos todas las páginas posibles de la página web
    for i in range(27): #hay 27 págians
        #combertimos la i a string para que se meta en el texto
        i = str(i+1)
        #cogemos la sopa del anterior método
        soup =obtener_conrtenido_pagina_web(str("https://www.elgusanitolector.com/libros-de/filosofia-26/?pagSel="+i+"&cuantos=30&orden=prioridad%2C+fecha_edicion+desc&codMateria=26&tipoArticulo=L"))
        # Crear variable para almacenar los elementos
        elemento_principal = soup.find("ul", {"class": "books grid"})
        #buscamos todos los elementos que está dentro del ul
        elementos = elemento_principal.find_all("li")

        # recorremos los elementos de la etiqueta y sacamos
        for elemento in elementos:
            #primero sacamos la portada
            imagen_url = elemento.find("img")["src"]
            # isbn = elemento.find("img")["src"] #la imagen contiene el ISBN en su URL
            # isbn = isbn.split("/")
            # isbn = isbn[-1][:12]
            #el nombre del libro
            nombre = elemento.find("img")["alt"] #el título está en una parte del html que se repite, pero en el alt de la imagen aparece el título
            #El autor está mal puesto, así que hay que hacerle unos cambios para que aparezca bonito
            #hacemos la búsqueda
            autor = elemento.find("dd", {"class":"creator"}).text[:-2].split("/")
            #creamos una variable para poner los autores bonitos
            autores = ""
            #contamos el número de autores
            contador = 1
            #recorremos los autores y modificamos lo que no nos gusta
            for i in autor:
                contador += 1
                #caundo llegue al último autor monle una y en vez de una ","
                if  contador == len(autor):
                    autores += i.strip(" ").capitalize() + " y "
                else:
                    autores += i.strip(" ").capitalize() + ", "

            #buscaamos el precio
            precio = float(elemento.find("strong").text[:-2].replace(",","."))

            #nos metemos en cada sección de cada libro, para ver los detalles de cada libro
            detalles_libro = obtener_conrtenido_pagina_web("https://www.elgusanitolector.com/"+elemento.find("a")["href"])

            #primero vemos su ISBN, pero como va variando en la posición las vamos recorriendo y vemos si cumple los requitos para ponerlo
            for i in range(len(detalles_libro.find_all("dd"))):
                if es_un_ISBN(detalles_libro.find_all("dd")[i].text):
                    isbn = detalles_libro.find_all("dd")[i].text

            #busacmos la sinopsis del libro, pero como algunas no tienen comprobamos si este tiene o no
            if detalles_libro.find("p", {"class": "bodytext"}) == None:
                descrippcion = "no tiene descrippción".encode("utf-8")
            else:
                descrippcion = detalles_libro.find ("div", {"id":"tabsinopsis"}).find("p", {"class": "bodytext"}).text.encode("utf-8")

            #vamos insertando a la lista con los libros los diccionarios con las características de cada libro
            nuevo_libro = libreria.copy()
            nuevo_libro["portada"] = imagen_url
            nuevo_libro["nombre"] = nombre
            nuevo_libro["autor"] = autores
            nuevo_libro["precio"] = precio
            nuevo_libro["descripcion"] = descrippcion.decode("utf-8")
            nuevo_libro["ISBN"] = isbn
            todos_libros.append(nuevo_libro)
            print(nuevo_libro)
    return todos_libros
print(extracxion_de_datos())