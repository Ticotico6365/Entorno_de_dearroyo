Algoritmo superercado
	//definimos las vaiables para el número aleatorio y para la compra
	Definir compra Como real
	Definir random_num Como Entero
	//generamos el número aleatorio
	random_num <- Aleatorio(0,500)
	//preguntamos la cantidad de la compra
	Escribir "inserte el precio de su compra: "
	Leer total
	Si random_num = 0 Entonces
		Escribir "como ", random_num, " es el número aleatorio y como ", random_num, "es menor que 100 su descuento será del 10%, por lo tantosu compra se quedará en: ", total - ((total*10)/100),"?";
	SiNo
		Si random_num > 100 Entonces
			Si random_num %2 = 0 Entonces
				Escribir "como ", random_num, " es el número aleatorio y como ", random_num, "es mayor que 100 su descuento será del 10%, pero como además es par, su descuento será del 12%, por lo tantosu compra se quedará en: ", total - ((total*12)/100),"?";
			SiNo
				Escribir "como ", random_num, " es el número aleatorio y como ", random_num, "es mayor que 100 su descuento será del 10%, pero como además es impar, su descuento será del 13%, por lo tantosu compra se quedará en: ", total - ((total*13)/100),"?";
			Fin Si
		SiNo
			Si random_num %2 = 0 Entonces
				Escribir "como ", random_num, " es el número aleatorio y como ", random_num, "es menor que 100 su descuento será del 20%, pero como además es par, su descuento será del 22%, por lo tantosu compra se quedará en: ", total - ((total*12)/100),"?";
			SiNo
				Escribir "como ", random_num, " es el número aleatorio y como ", random_num, "es menor que 100 su descuento será del 20%, pero como además es impar, su descuento será del 23%, por lo tantosu compra se quedará en: ", total - ((total*13)/100),"?";
			Fin Si
		Fin Si
	Fin Si
	
FinAlgoritmo
