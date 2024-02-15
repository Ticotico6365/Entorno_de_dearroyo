package org.example.PrimeraVez;

import java.util.Locale;

public class Funciones {


    //def suma (a,b):
    //  return a + b

    public static Integer suma (Integer a, Integer b){
        return a + b;
    }

    //def pasa_minúscula (etxto)
    //  etxto_en_minúsculas = texto.lower()
    //  return  etxto_en_minúsculas

    public static String pasaMinusculas (String text){
        String textoEnMinusculas = text.toLowerCase();
        return textoEnMinusculas;
    }
    public static void main(String[] args) {

        System.out.println(suma(8,9));

        System.out.println(pasaMinusculas("FELIZ NAVIDAD"));

    }


}
