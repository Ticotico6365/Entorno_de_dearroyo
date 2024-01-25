Algoritmo Ejercicio_4
	Escribir "Bienvenido a Ejercicio 4 donde sabremos cual es el número mayor"
	
	Escribir "De un valor a su variable a, por favor:"
	Leer a
	
	Escribir "Ahora de un valor a su variable b, por favor:"
	Leer b

	Si a = b Entonces
		grande <- 0
	SiNo
		Si a > b Entonces
			grande <- 1
		SiNo
			Si a < b Entonces
				grande <- -1
			SiNo
				
			Fin Si
		Fin Si
	Fin Si
	Escribir "Ahora de un valor a su variable c, por favor:"
	Leer c
	
	Si b = c y grande = 0 Entonces
		Escribir "los tres son iguales"
	SiNo
		Si  b > c y grande = 0 Entonces
			Escribir "a = b > c"
		SiNo
			Si b < c y grande = 0 Entonces
				Escribir "a = b < c"
			SiNo
				Si b = c y grande = 1 Entonces
					Escribir "a > b = c"
				SiNo
					Si b > c y grande = 1 Entonces
						Escribir "a > b > c"
					SiNo
						Si b < c y grande = 1 Entonces
							Escribir "a > c > b"
						SiNo
							Si b = c y grande = -1 Entonces
								Escribir "a < b = c"
							SiNo
								Si b > c y grande = -1 Entonces
									Escribir "a < b > c"
								SiNo
									Si b < c y grande = -1 Entonces
										Escribir "a < b < c"
									SiNo
										
									Fin Si
								Fin Si
							Fin Si
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
