package org.example.Practica2;

import java.util.ArrayList;
import java.util.List;

public class main {
    public static void main(String[] args) {

        //ejercicio 1: Recibe una lista y un elemento, y agrega el elemento al final de la lista.
        List<String> miLista = new ArrayList<>();
        System.out.println(ManipuladorDeListas.AgregaElemento(miLista, "solomillo"));

        //ejercicio 2: Recibe una lista y un elemento, y elimina la primera ocurrencia del elemento en la lista.
        List<String> lista2 = new ArrayList<>(List.of("pera","mango","platano"));
        System.out.println(ManipuladorDeListas.EliminaElemento(lista2, "pera"));

        //ejercicio 3: Recibe una lista y un índice, y devuelve el elemento en la posición especificada por el índice.
        List<String> lista3 = new ArrayList<>(List.of("pedro", "luis", "jonás", "antonio", "pedro luis"));
        System.out.println(ManipuladorDeListas.IndiceLista(lista3, 3));

        //ejercicio 4: Recibe una lista y devuelve una nueva lista con los elementos invertidos.
        List<String> lista4 = new ArrayList<>(List.of("pedro", "luis", "jonás", "antonio", "pedro luis"));
        System.out.println(ManipuladorDeListas.IvertirLista(lista4));

        //ejercicio 5: Recibe una lista y devuelve el número de elementos presentes en ella.
        List<String> lista5 = new ArrayList<>(List.of("pedro", "luis", "jonás", "antonio", "pedro luis"));
        System.out.println(ManipuladorDeListas.ContarLista(lista5));

        //ejercicio 6: Recibe dos listas y devuelve una nueva lista que es la concatenación de ambas.
        List<String> lista6 = new ArrayList<>(List.of("pedro", "luis", "jonás", "antonio", "pedro luis"));
        List<String> lista7 = new ArrayList<>(List.of("pera","mango","platano"));
        System.out.println(ManipuladorDeListas.DosListas(lista6, lista7));

        //ejercicio 7: Este método verifica si una lista es un palíndromo, es decir, si se mantiene igual al invertirla.
        List<String> lista8 = new ArrayList<>(List.of("pedro", "luis", "jonás", "antonio", "pedro luis", "pedro luis", "antonio", "jonás", "luis", "pedro"));
        System.out.println(ManipuladorDeListas.ListaPalindomo(lista8));

        //ejercicio 8: Este método devuelve el número de veces que un elemento específico aparece en una lista.
        List<String> lista9 = new ArrayList<>(List.of("pedro", "luis", "jonás", "antonio", "pedro luis", "pedro luis", "antonio", "jonás", "luis", "pedro", "luis", "luis"));
        System.out.println(ManipuladorDeListas.NumElemento(lista9, "luis"));
    }
}
