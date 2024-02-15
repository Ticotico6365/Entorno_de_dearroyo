"""
todas las variables que estoy usando
tiene que ver con panaderías o con comida.
"""
pollo = "Bienvenidos a Pyhithon"
polvillo = 7
panadería_polvilo = "calle calatraba"
pan = 4
separacion = "_"  # la he creado para separar, no es un ejemplo.
# estoy declarando una variable en la que no hay ningún valor
aqui_no_hay_nada = None
variable_binario = True
variable_lista = [1, 2, 3, "pepe", 4, False]

print(pollo)
print(variable_binario)

print(separacion.center(50, "_"))

bar = "00000014578"

print(panadería_polvilo.center(50, "/"))

bar_convertido_a_numero = int(bar)
print(bar)
print(bar_convertido_a_numero)

print(separacion.center(50, "_"))

balon = 23
balon_cadena = str(balon)
balon_decimal = float(balon)
balon_boolean = bool(balon)

print(balon)
print(balon_cadena)
print(balon_decimal)
print(balon_boolean)

print(separacion.center(50, "_"))

valon = 23.45
valon_cadena = str(valon)
valon_decimal = int(valon)
valon_boolean = bool(valon)

print(valon)
print(valon_cadena)
print(valon_decimal)
print(valon_boolean)

print(separacion.center(50, "_"))

jalon = True
jalon_cadena = str(jalon)
jalon_decimal = int(jalon)
jalon_boolean = float(jalon)

print(jalon)
print(jalon_cadena)
print(jalon_decimal)
print(jalon_boolean)

print(separacion.center(50, "_"))

numero = 0

numero += 3

print(numero)

print(separacion.center(50, "_"))

if numero == 3:
    print("el número es igual a 3")
else:
    print("no es igual")

print(separacion.center(50, "_"))


def saludar():
    print("hola amigos!!!")


"""
si no se llama al método, no se ejecuta
"""

saludar()


def alba():
    contador_ninias_segundo = 2
    return contador_ninias_segundo


def alberto():
    conatdor_niñas_primero = 5
    suma = conatdor_niñas_primero + alba()
    contador_alba = alba()
    print(suma)
    print(contador_alba)


alba()
"""
al imprimir se pierde información, con return se guarda, pero no aparece en consola
"""
alberto()

print(separacion.center(50, "_"))


def david():
    contador_nnias_segundo = 2
    return contador_nnias_segundo


def alejandro(trapicheo):
    conatdor_nnias_primero = 5
    print(conatdor_nnias_primero + trapicheo)


alejandro(0)

print(separacion.center(50, "_"))


def ejercicio_1(texto):
    return texto.lower()


print(ejercicio_1("HOLA"))