Algoritmo porcentaje_nino_nina
	//definimos las vaiables para el n�mero de ni�os y ni�as
	Definir num_nino Como Entero
	Definir num_nina Como Entero
	//pedimos al usuario que inserte el n�mero de ni�os que hay
	Escribir "Inserte el n�emro de ni�os: ";
	Leer num_nino
	//Pedimos al usuario el n�mero de ni�as que hay
	Escribir "Inserte el n�emro de ni�as: ";
	Leer num_nina
	//escribimos directamente el porcentage, que al final es el n�mero de ni�o/a entre la suma entre ambos, todo multiplicado por 100
	Escribir "El porcentage de ni�os es del ", trunc((num_nino/(num_nina+num_nino))*100),"%";

	//vemos si el porcentage del n�mero de ni�os es par o impar
	Si (num_nino/(num_nina+num_nino))*100 = 0 Entonces
		Escribir "no es par ni impar";
	SiNo
		//antes de ver si el n�mero es par o impar es necesario truncar
		Si trunc((num_nino/(num_nina+num_nino))*100)%2 = 0 Entonces
			Escribir "El porcentaje del n�mero de ni�os es par"
		SiNo
			Escribir "El porcentaje del n�mero de ni�os es impar"
		Fin Si
	Fin Si
	
	Escribir "El porcentage de ni�as es del ", trunc((num_nina/(num_nina+num_nino))*100),"%";
	//vemos si el porcentage del n�mero de ni�as es par o impar
	Si (num_nina/(num_nina+num_nino))*100 = 0 Entonces
		Escribir "no es par ni impar";
	SiNo
		//antes de ver si el n�mero es par o impar es necesario truncar
		Si trunc((num_nina/(num_nina+num_nino))*100)%2 = 0 Entonces
			Escribir "El porcentaje del n�mero de ni�as es par"
		SiNo
			Escribir "El porcentaje del n�mero de ni�as es impar"
		Fin Si
	Fin Si
FinAlgoritmo
