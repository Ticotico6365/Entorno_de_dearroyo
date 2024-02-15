import java.util.ArrayList;
import java.util.List;

public class Text {
    public static void main(String[] args) {

        List<String> palabras = new ArrayList<>();
        palabras.add("Hola");
        palabras.add("Mundo");
        palabras.add("Java");
        palabras.add("Programación");
        palabras.add("Java");

        List<Integer> numeros = new ArrayList<>();
        numeros.add(5);
        numeros.add(10);
        numeros.add(20);
        numeros.add(7);

        //System.out.println(ManipuladorDeListas.agregarElementoFinal(numeros, 3));

        //System.out.println(ManipuladorDeListas.eliminarElementoPorObjetoRepetido(palabras, "Java"));

        //System.out.println(ManipuladorDeListas.concatenarListas(palabras,palabras));

        //System.out.println(ManipuladorDeListas.contarElementosEspecificos(palabras, "Java"));

        System.out.println(ManipuladorDeListas.obtenerSublista(palabras, 2,3));
        System.out.println(palabras.subList(2,3));

    }
}
