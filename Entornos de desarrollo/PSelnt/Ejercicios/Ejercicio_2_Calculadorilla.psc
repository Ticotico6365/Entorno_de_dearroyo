Algoritmo Calculadorilla_Ejercicio_2
	Escribir "Bienvenido a Calculadorilla"
	
	Escribir "De un valor a su variable a, por favor:"
	Leer a
	
	Escribir "Ahora de un valor a su variable b, por favor:"
	Leer b
	
	Escribir "Si sumamos a y b nos da ", a + b
	Escribir "Si restamos a menos b nos da ", a - b
	Escribir "Si restamos b menos a nos da ", b - a
	Escribir "Si multiplicamos a por b nos da ", a * b
	
	Si a = 0 Entonces
		Escribir "Eres tonto o te lo haces no se puede dividir nada entre 0"
	SiNo
		Escribir "Si dividimos b entre a nos da ", b / a
	Fin Si
	
	Si b = 0 Entonces
		Escribir "Eres tonto o te lo haces no se puede dividir nada entre 0"
	SiNo
		Escribir "Si dividimos a entre b nos da ", a / b
	Fin Si
	
FinAlgoritmo
