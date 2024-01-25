import requests
import bs4

def obtener_conrtenido_pagina_web_cometas():

    #hacemos petición a la url de la página web para obtener su HTML
    pagina_html = requests.get("https://hqkitesusa.com/products.asp?cat=115")

    #Analizamos el HTML obtenido con bs4ç
    soup = bs4.BeautifulSoup(pagina_html.content, "html.parser")

    #Devolvemos la sopa de bs4
    return soup

def extracxion_de_datos_cometas():

    #sopa de mi página web
    soup = obtener_conrtenido_pagina_web_cometas()
    #Crear variable para almacenar los elementos
    elementos = soup.find_all("div", {"class" : "product"})
    #recorremos los elementos de la etiqueta y sacamos
    for elemento in elementos:
        nombre = elemento.find("img")["alt"] #como el nombre de la cometa está dentro de la imagen
        precio = elemento.find("span", {"class" : "price"}).text #el precio está en es texto del spam
        print(precio, nombre)

extracxion_de_datos_cometas()

def obtener_conrtenido_pagina_web_libros():

    #hacemos petición a la url de la página web para obtener su HTML
    pagina_html = requests.get("https://www.elgusanitolector.com/libros-de/filosofia-26/")

    #Analizamos el HTML obtenido con bs4ç
    soup = bs4.BeautifulSoup(pagina_html.content, "html.parser")

    #Devolvemos la sopa de bs4
    return soup

def extracxion_de_datos_libros():

    #sopa de mi página web
    soup = obtener_conrtenido_pagina_web_libros()
    #Crear variable para almacenar los elementos
    elementos = soup.find_all("div", {"class" : "item"})
    #recorremos los elementos de la etiqueta y sacamos
    for elemento in elementos:
        nombre = elemento.find("a") #como el nombre de la cometa está dentro de la imagen
        precio = elemento.find("span", {"class" : "price"}).text #el precio está en es texto del spam
        print(precio, nombre)

extracxion_de_datos_libros()