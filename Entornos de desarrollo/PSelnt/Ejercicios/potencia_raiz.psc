Proceso potencia_raiz //ejercicio6
	Definir x Como Real;
	Escribir "Escriba su número: ";
	Leer x;
	Si x = 0 Entonces
		Escribir "Perdona, pero la raiz de 0 no existe";
	SiNo
		Escribir "Del numero ", x, " su potencia es ", x^2, " y su raíz ", raiz(x);
	FinSi
FinProceso