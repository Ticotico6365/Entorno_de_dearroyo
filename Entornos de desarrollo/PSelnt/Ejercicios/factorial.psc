Proceso factorial
	Definir a Como Entero;
	Definir resultado Como Entero;
	Definir contador Como Entero;
	Leer a;
	Repetir
		contador<-contador + 1;
		a <- a*(a-1);
		a <- resultado;
	Hasta Que contador = a
	Escribir resultado;
FinProceso
