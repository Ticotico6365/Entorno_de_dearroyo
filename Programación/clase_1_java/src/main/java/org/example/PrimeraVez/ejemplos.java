package org.example.PrimeraVez;

public class ejemplos {

    public static void main(String[] args) { //main para que me apezca lo básico
        //variables
        int num = 3;
        //tipos
        int numero_entero = 8; //nunca pueden ser nulo
        double numero_decimal = 5.6; //nunca pueden ser nulo
        boolean booleano = true; //nunca pueden ser nulo

        String cadena = "Hola"; //pueden ser nulo
        Integer numero = null; //pueden ser nulo
        Double decimal = 8.9; //pueden ser nulo
        Boolean valor = false; //pueden ser nulo

        //print
        System.out.println("Feliz Navidad");
        //sout para que me aparezca lo de arriba


        //condicionales
        // and -> &&
        // or -> || (Alt GR + 1 = |)

        Integer num1 = 5;
        Integer num2 = 7;

        Integer numa = num1 +  num2;

        if (num1 < num2 && numero != null) {
            System.out.println("el número 1 es mayor");
        } else if (num1 == num2) {
            System.out.println("los números son iguales");
        }else {
            System.out.println("el número 2 es mayor");
        }

        //bucle

        //for i in range(7):
        //1.- declaras el nombre de la vaiable ; 2.- hasta que llege al número ; 3.- cómo se incremaenta mi variable
        for(int i = 0; i < 7; i+=2) { //si pones 2 veces + se suma de uno en uno
            System.out.println(i);
        }


        // for i in colores:
        // in -> :
        // Hay que declararla e indicar su tipo
        // Srting -> noo se pueden tratar como listas -> hay que pasarlo a lista char()  -> toCharArray
        for(Character i: cadena.toCharArray()){
            System.out.println(i);
        }

        //Bucles no limitados
        Integer ncontador = 10;
        while (ncontador != 0){
            System.out.println(ncontador);
            ncontador --; // con el -- es igual que poner -= 1
        }

        //combresiones
        String cadenaContador = String.valueOf(ncontador);
    }
}
