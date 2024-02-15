package org.example.Practica1;

public class Main {
    public static void main(String[] args) {

        //ejercicio 1 Recibe una cadena y devuelve la cadena en minúsculas.
        String cadenaAMinuscula = ManipuladorDeCadenas.pasarAMinuscula("MI PRIMER TEXTO EN JAvA");
        System.out.println(cadenaAMinuscula);

        //ejercicio 2 Recibe una cadena y devuelve la cadena en mayúsculas.
        String cadenaAMayuscula= ManipuladorDeCadenas.pasarAMayuscula("mi primer texto en jaVa");
        System.out.println(cadenaAMayuscula);

        //ejercicio 3 Recibe una cadena y devuelve la cadena invertida.
        String cadenaInvertida= ManipuladorDeCadenas.invertirCadena("mi primer texto en jaVa");
        System.out.println(cadenaInvertida);

        //ejercicio 4
        Integer numVocales= ManipuladorDeCadenas.contadorVocales("aeiougggggggggaeiou");
        System.out.println(numVocales.toString());

    }
}
