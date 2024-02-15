package org.example.Practica2;

import java.util.ArrayList;
import java.util.List;

public class ManipuladorDeListas {
    //ejercicio 1: Recibe una lista y un elemento, y agrega el elemento al final de la lista.
    public static List<String> AgregaElemento (List<String>lista , String elemento){
        lista.add(elemento);
        return lista;
    }

    //ejercicio 2: Recibe una lista y un elemento, y elimina la primera ocurrencia del elemento en la lista.
    public static List<String> EliminaElemento (List<String>lista, String elemento){
        lista.remove(elemento);
        return lista;
    }
    //ejercicio 3: Recibe una lista y un índice, y devuelve el elemento en la posición especificada por el índice.
    public static String IndiceLista (List<String> lista, int indice){
        String elemento = lista.get(indice);
        return elemento;
    }
    //ejericio 4: Recibe una lista y devuelve una nueva lista con los elementos invertidos.
    public static List<String> IvertirLista (List<String> lista){
        List<String> nuevaLista = new ArrayList<>();

        for (int i = lista.size() - 1; i >= 0; i--){
            nuevaLista.add(IndiceLista(lista, i));
        }
        return nuevaLista;

    }
    //ejercicio 5:Recibe una lista y devuelve el número de elementos presentes en ella.
    public static Integer ContarLista (List<String> lista ){
        Integer siceLista = lista.size();
        return siceLista;
    }
    //ejercicio 6: Recibe dos listas y devuelve una nueva lista que es la concatenación de ambas.
    public static List<String> DosListas (List<String> lista1, List<String> list2){
        lista1.addAll(list2);
        return lista1;
    }
    //ejercicio 7: Este método verifica si una lista es un palíndromo, es decir, si se mantiene igual al invertirla.
    public static Boolean ListaPalindomo (List<String> lista){
        Integer palindromo = 0;
        List<String> listaInversa = IvertirLista(lista);

        for (int i = 0 ;i < lista.size();i++){
            if (lista.get(i) == listaInversa.get(i)){
                palindromo ++;
            }
        }
        return palindromo == lista.size();
    }
    //ejercicio 8: Este método devuelve el número de veces que un elemento específico aparece en una lista.
    public static Integer NumElemento (List<String> lista, String elemento){
        lista.retainAll(List.of(elemento));
        Integer numElemento = lista.size();
        return numElemento;
    }
    //ejercicio 9: Este método recibe una lista y elimina los elementos duplicados, dejando solo una ocurrencia de cada elemento.
}
