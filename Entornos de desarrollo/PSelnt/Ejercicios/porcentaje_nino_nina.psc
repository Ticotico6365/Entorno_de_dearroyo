Algoritmo porcentaje_nino_nina
	//definimos las vaiables para el número de niños y niñas
	Definir num_nino Como Entero
	Definir num_nina Como Entero
	//pedimos al usuario que inserte el número de niños que hay
	Escribir "Inserte el núemro de niños: ";
	Leer num_nino
	//Pedimos al usuario el número de niñas que hay
	Escribir "Inserte el núemro de niñas: ";
	Leer num_nina
	//escribimos directamente el porcentage, que al final es el número de niño/a entre la suma entre ambos, todo multiplicado por 100
	Escribir "El porcentage de niños es del ", trunc((num_nino/(num_nina+num_nino))*100),"%";

	//vemos si el porcentage del número de niños es par o impar
	Si (num_nino/(num_nina+num_nino))*100 = 0 Entonces
		Escribir "no es par ni impar";
	SiNo
		//antes de ver si el número es par o impar es necesario truncar
		Si trunc((num_nino/(num_nina+num_nino))*100)%2 = 0 Entonces
			Escribir "El porcentaje del número de niños es par"
		SiNo
			Escribir "El porcentaje del número de niños es impar"
		Fin Si
	Fin Si
	
	Escribir "El porcentage de niñas es del ", trunc((num_nina/(num_nina+num_nino))*100),"%";
	//vemos si el porcentage del número de niñas es par o impar
	Si (num_nina/(num_nina+num_nino))*100 = 0 Entonces
		Escribir "no es par ni impar";
	SiNo
		//antes de ver si el número es par o impar es necesario truncar
		Si trunc((num_nina/(num_nina+num_nino))*100)%2 = 0 Entonces
			Escribir "El porcentaje del número de niñas es par"
		SiNo
			Escribir "El porcentaje del número de niñas es impar"
		Fin Si
	Fin Si
FinAlgoritmo
