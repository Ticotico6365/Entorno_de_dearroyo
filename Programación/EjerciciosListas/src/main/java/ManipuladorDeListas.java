import java.util.ArrayList;
import java.util.List;

public class ManipuladorDeListas {

    public static List<Integer> agregarElementoFinal (List<Integer> listaNumeros, Integer numeroNuevo){

        listaNumeros.add(numeroNuevo);

        return listaNumeros;

    }

    public static List<String> eliminarElementoPorObjeto (List<String> listapalabras, String palabraNuevo){
        listapalabras.remove(palabraNuevo);

        return listapalabras;
    }
    public static List<String> eliminarElementoPorIndice (List<String> listaPalabras, int indice){
        listaPalabras.remove(indice);

        return listaPalabras;
    }

    public static List<String> eliminarElementoPorObjetoRepetido (List<String> listaPalabras, String palabraNuevo){

        while (listaPalabras.contains(palabraNuevo)){
                eliminarElementoPorObjeto(listaPalabras,palabraNuevo);
        }
        return listaPalabras;

    }

    public static String obtenerElemento (List<String> listaPalabras, int indice){

        return listaPalabras.get(indice);
    }

    public static List<String> invertirLista (List<String> listaPalabras){

        return listaPalabras.reversed();
    }

    public static List<String> concatenarListas (List<String> list1, List<String> list2){

        list1.addAll(list2);

        return list1;

    }


    public static boolean esListaPalindromo(List<String> list){
        return list == list.reversed();
    }

    public static Integer contarElementosEspecificos (List<String> list, String palabra){
        Integer contador = 0;
        while (list.contains(palabra)){
            list.remove(palabra);
            contador++;
        }

        return contador;
    }

    public static List<String> obtenerSublista ( List<String> list, int num1, int num2){

        return list.subList(num1, num2);
    }



}
