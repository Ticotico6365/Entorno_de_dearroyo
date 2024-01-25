
"""
Condicionales
"""
es_hombre = True
es_mujer = True
pelo_rubio = True
pelo_moreno = False
cantante = False
deportista = True


if es_hombre:
    if pelo_rubio:
        if deportista:
            print ("ES GUTI!!")
        elif cantante:
            print("Dani Martín!!!")
        else:
            print("ES BRAD PITT!!")

else:
    print("Es mujer!!")