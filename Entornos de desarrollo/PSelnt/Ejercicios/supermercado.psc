Proceso supermercado //actividadd 3
	Definir a Como Entero;
	Definir total Como Real;
	Escribir "meta el precio tatal de la compra";
	Leer total;
	a<-Aleatorio(0,148);
	si a < 74 Entonces
		Escribir "Como el número que a salido es ",a ," y este es menor que 74, su compra de ", total, "? se quedaría con un descuento del 15% a ", -((total*15)/100)+total, "?";
	SiNo
		Escribir "Como el número que a salido es ",a ," y este es mayor que 74, su compra de ", total, "? se quedaría con un descuento del 20% a ", -((total*20)/100)+total, "?";
	FinSi
	
FinProceso
