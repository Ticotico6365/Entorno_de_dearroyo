def num_puntuacion (text):
    #declaramos las variables que se van a guardar el número de caracteres deseados.
    #primero las que se hacen facil, porque no hay normas distintas
    num_comas = text.count(",")
    num_guiones = text.count("-")
    num_dos_puntos = text.count(":")
    num_punto_coma = text.count(";")
    num_dieresis = text.count("ü")
    #ahora las complicadas
    num_tres_puntos = text.count("...")
    num_puntos = text.count(".")-3*num_tres_puntos
    num_parentesis = text.count("(")
    num_corchetes = text.count("[")
    num_interrogaciones = text.count("¿")
    num_exclamaciones = text.count("¡")
    num_comillas = text.count('"')/2
    print("Signos de puntuación encontrados:")
    if num_comas != 0:
        print("Número de comas: ",num_comas)
    if num_puntos != 0:
        print("Número de puntos: ",num_puntos)
    if num_interrogaciones != 0:
        print("Número de signos de interrogación: ",num_interrogaciones)
    if num_dos_puntos != 0:
        print("Número dos puntos: ",num_dos_puntos)
    if num_exclamaciones != 0:
        print("Número de signos de exclamación: ",num_exclamaciones)
    if num_guiones != 0:
        print("Número de guiones: ",num_guiones)
    if num_punto_coma != 0:
        print("Número de punto y coma: ",num_punto_coma)
    if num_dieresis != 0:
        print("Número de dieresis: ",num_dieresis)
    if num_dieresis != 0:
        print("Número de dieresis: ",num_dieresis)
    if num_parentesis != 0:
        print("Número de paréntesis: ",num_parentesis)
    if num_corchetes != 0:
        print("Número de corchetes: ",num_corchetes)
    if num_comillas != 0:
        print("Número de comittas: ",num_comillas)

# num_puntuacion("""
# Con diez cañones por banda,
# viento en popa a toda vela,
# no corta el mar, sino vuela
# un velero bergantín;
#
# bajel pirata que llaman,
# por su bravura, el Temido,
# en todo mar conocido
# del uno al otro confín.
#
# La luna en el mar riela,
# en la lona gime el viento
# y alza en blando movimiento
# olas de plata y azul;
#
# y va el capitán pirata,
# cantando alegre en la popa,
# Asia a un lado, al otro Europa,
# y allá a su frente Estambul.
#
# «Navega velero mío,
# sin temor,
# que ni enemigo navío,
# ni tormenta, ni bonanza,
# tu rumbo a torcer alcanza,
# ni a sujetar tu valor.
#
# Veinte presas
# hemos hecho
# a despecho,
# del inglés,
#
# y han rendido
# sus pendones
# cien naciones
# a mis pies.
#
# Que es mi barco mi tesoro,
# que es mi dios la libertad,
# mi ley, la fuerza y el viento,
# mi única patria la mar.
#
# Allá muevan feroz guerra
# ciegos reyes
# por un palmo más de tierra,
# que yo tengo aquí por mío
# cuanto abarca el mar bravío,
# a quien nadie impuso leyes.
#
# Y no hay playa,
#
# sea cualquiera,
# ni bandera
# de esplendor,
#
# que no sienta
# mi derecho
# y dé pecho
# a mi valor...
#
# Que es mi barco mi tesoro,
# que es mi dios la libertad,
# mi ley, la fuerza y el viento,
# mi única patria la mar.
#
# A la voz de ¡barco viene!
# es de ver
# cómo vira y se previene
# a todo trapo a escapar:
# que yo soy el rey del mar,
# y mi furia es de temer.
#
# En las presas
# yo divido
# lo cogido
# por igual:
#
# sólo quiero
# por riqueza
# la belleza
# sin rival.
#
# Que es mi barco mi tesoro,
# que es mi dios la libertad,
# mi ley, la fuerza y el viento,
# mi única patria la mar.
#
# ¡Sentenciado estoy a muerte!;
# yo me río;
# no me abandone la suerte,
# y al mismo que me condena,
# colgaré de alguna antena
# quizá en su propio navío.
#
# Y si caigo
# ¿qué es la vida?
# Por perdida
# ya la di,
#
# cuando el yugo
# de un esclavo
# como un bravo
# sacudí.
#
# Que es mi barco mi tesoro,
# que es mi dios la libertad,
# mi ley, la fuerza y el viento,
# mi única patria la mar.
#
# Son mi música mejor
# aquilones,
# el estrépito y temblor
# de los cables sacudidos,
# del negro mar los bramidos
# y el rugir de mis cañones.
#
# Y del trueno
# al son violento,
# y del viento
# al rebramar,
#
# yo me duermo
# sosegado
# arrullado
# por el mar.
#
# Que es mi barco mi tesoro,
# que es mi dios la libertad,
# mi ley, la fuerza y el viento,
# mi única patria la mar».
# """)

def ejercicio_lista ():
    usuario = [{
        "nombre": "Enrique",
        "apellidos": "García, Migueza",
        "dni": "12345678K",
        "email": "egarciamigueza@safareyes.es"
    },
    {
        "nombre": "Paloma",
        "apellidos": "Machado, López",
        "dni": "12345678Z",
        "email": "pmachadolopez@hotmail.es"
    },
    {
        "nombre": "Antonio",
        "apellidos": "Romero, Domínguez",
        "dni": "12345678A",
        "email": "aromerodominguez@safareyes.es"
    }]
    lista_usuarios_email = []
    lista_apelidos = []
    lista_dni = []
    for i in usuario:
        if "@safareyes.es" in i["email"]:
            lista_usuarios_email.append(i)

        lista_apelidos.append(i["apellidos"].split(",")[0])

        lista_dni.append(i["dni"][-1])

    lista_apelidos.sort()
    lista_dni.sort()

    return lista_usuarios_email, lista_apelidos[0], usuario[usuario["dni"][-1]]

print(ejercicio_lista())