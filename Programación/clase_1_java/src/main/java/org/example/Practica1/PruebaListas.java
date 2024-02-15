package org.example.Practica1;

import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.List;

public class PruebaListas {
    public static void main(String[] args) {

        //creacion y definición de listas
        //lista = ["verde, "rojo", "vede"]

        List<String> lista = new ArrayList<>();

        //Añadir elementos
        lista.add("Verde");
        lista.add("Rojo");
        lista.add("Azul");
        lista.add("Amarillo");
        lista.add("Amarillo");
        lista.add("Amarillo");
        lista.add("Morado");

        lista.add(2, "naranja");
        //lista.set(2, "púrpura");

        lista.addAll(List.of("lila", "marrón", "dorado"));

        //eliminar
        lista.remove("Amarillo");
        lista.removeAll(List.of("Amarillo", "Azul"));
        lista.remove(0);


        //obtener elementos
        System.out.println(lista.get(2));
        System.out.println(lista);


    }



}
