Algoritmo superercado
	//definimos las vaiables para el n�mero aleatorio y para la compra
	Definir compra Como real
	Definir random_num Como Entero
	//generamos el n�mero aleatorio
	random_num <- Aleatorio(0,500)
	//preguntamos la cantidad de la compra
	Escribir "inserte el precio de su compra: "
	Leer total
	Si random_num = 0 Entonces
		Escribir "como ", random_num, " es el n�mero aleatorio y como ", random_num, "es menor que 100 su descuento ser� del 10%, por lo tantosu compra se quedar� en: ", total - ((total*10)/100),"?";
	SiNo
		Si random_num > 100 Entonces
			Si random_num %2 = 0 Entonces
				Escribir "como ", random_num, " es el n�mero aleatorio y como ", random_num, "es mayor que 100 su descuento ser� del 10%, pero como adem�s es par, su descuento ser� del 12%, por lo tantosu compra se quedar� en: ", total - ((total*12)/100),"?";
			SiNo
				Escribir "como ", random_num, " es el n�mero aleatorio y como ", random_num, "es mayor que 100 su descuento ser� del 10%, pero como adem�s es impar, su descuento ser� del 13%, por lo tantosu compra se quedar� en: ", total - ((total*13)/100),"?";
			Fin Si
		SiNo
			Si random_num %2 = 0 Entonces
				Escribir "como ", random_num, " es el n�mero aleatorio y como ", random_num, "es menor que 100 su descuento ser� del 20%, pero como adem�s es par, su descuento ser� del 22%, por lo tantosu compra se quedar� en: ", total - ((total*12)/100),"?";
			SiNo
				Escribir "como ", random_num, " es el n�mero aleatorio y como ", random_num, "es menor que 100 su descuento ser� del 20%, pero como adem�s es impar, su descuento ser� del 23%, por lo tantosu compra se quedar� en: ", total - ((total*13)/100),"?";
			Fin Si
		Fin Si
	Fin Si
	
FinAlgoritmo
