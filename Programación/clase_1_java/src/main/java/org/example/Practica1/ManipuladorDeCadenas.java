package org.example.Practica1;

public class ManipuladorDeCadenas {
    //ejercicio 1
    public static String pasarAMinuscula (String text){
        return text.toLowerCase();
    }
    //ejercicio 2
    public static String pasarAMayuscula (String text){
        return text.toUpperCase();
    }
    //ejercicio 3
    public static String invertirCadena (String text){
//        String invertido = "";
//        for (int i = text.length() - 1; i >= 0; i--) {
//            invertido += text.charAt(i);
//        }
//        return invertido;

        // convertimos nuestro texto a string builder
        StringBuilder textoBuilder = new StringBuilder(text);

        return textoBuilder.reverse().toString(); // el .reverse le da la vuelta a la cadena y el .toString pasa el objeto a String

    }
    public static Integer contadorVocales (String text){
        Integer contador = 0;

        for (char i: text.toCharArray()){
            if (i == 'a' || i == 'e' || i == 'i' || i == 'o' || i == 'u'){
                contador++;
            }
        }

        return contador;

    }


}
