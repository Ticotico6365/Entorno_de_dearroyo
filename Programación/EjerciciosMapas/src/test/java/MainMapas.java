import java.util.HashMap;
import java.util.Map;

public class MainMapas {
    public static void main(String[] args) {

        // creamos el mapa
        Map<String, String> mapaAnime = new HashMap<>();
        mapaAnime.put("Naruto", "Naruto Shippuden");
        mapaAnime.put("Luffy", "One Piece");
        mapaAnime.put("Goku", "Dragon Ball");
        mapaAnime.put("Eren", "Attack on Titan");
        mapaAnime.put("Deku", "My Hero Academia");
        mapaAnime.put("Light", "Death Note");
        mapaAnime.put("Saitama", "One Punch Man");
        mapaAnime.put("Ash", "Pokemon");
        mapaAnime.put("Shinji", "Neon Genesis Evangelion");
        mapaAnime.put("Edward", "Fullmetal Alchemist");
        //System.out.println(mapaAnime);

        // creamos otro mapa
        Map<String, String> mapaCoches = new HashMap<>();
        mapaCoches.put("Model S", "Tesla");
        mapaCoches.put("3 Series", "BMW");
        mapaCoches.put("Civic", "Honda");
        mapaCoches.put("Corolla", "Toyota");
        mapaCoches.put("Mustang", "Ford");
        mapaCoches.put("911", "Porsche");
        mapaCoches.put("Aventador", "Lamborghini");
        mapaCoches.put("Veyron", "Bugatti");
        mapaCoches.put("Phantom", "Rolls-Royce");
        mapaCoches.put("F-Type", "Jaguar");
        mapaCoches.put("Ford-T", "Ford");
        //System.out.println(mapaCoches);

        Map<String, String> mapaNull = new HashMap<>();
        mapaNull.put("Juan", "Ingeniero");
        mapaNull.put("Ana", "Doctora");
        mapaNull.put("Carlos", null);
        mapaNull.put("María", "Profesora");
        mapaNull.put("Pedro", "Arquitecto");
        mapaNull.put("Laura", null);
        mapaNull.put(null, "Abogado");
        mapaNull.put("Sofía", "Diseñadora");
        mapaNull.put("Luis", "Programador");
        mapaNull.put("Carmen", "Periodista");
        //Prueba ejercicio 1
        System.out.println("----------Ejercicio 1----------");

        ManipuladorMapas.agregarElemento(mapaAnime,"David","Ciberpunk 2077");
        System.out.println(mapaAnime);

        ManipuladorMapas.agregarElemento(mapaCoches,"gtr","Nissan");
        System.out.println(mapaCoches);

        //Ejercicio 2
        System.out.println("----------Ejercicio 2----------");

        ManipuladorMapas.eliminarElemento(mapaAnime,"David");
        System.out.println(mapaAnime);

        ManipuladorMapas.eliminarElemento(mapaCoches,"gtr");
        System.out.println(mapaCoches);

        //Ejericio 3
        System.out.println("----------Ejercicio 3----------");

        System.out.println(ManipuladorMapas.obtenerElemento(mapaAnime,"Naruto"));

        System.out.println(ManipuladorMapas.obtenerElemento(mapaCoches,"911"));

        //Ejercicio 4
        System.out.println("----------Ejercicio 4----------");

        System.out.println(ManipuladorMapas.contarElementos(mapaAnime));

        System.out.println(ManipuladorMapas.contarElementos(mapaCoches));

        //Ejercicio 5
        System.out.println("----------Ejercicio 5----------");

        System.out.println(ManipuladorMapas.verificarExistenciaClave(mapaAnime,"Deku"));
        System.out.println(ManipuladorMapas.verificarExistenciaClave(mapaAnime,"David"));

        System.out.println(ManipuladorMapas.verificarExistenciaClave(mapaCoches,"Ford-T"));
        System.out.println(ManipuladorMapas.verificarExistenciaClave(mapaCoches,"gtr"));

        //Ejercicio 6
        System.out.println("----------Ejercicio 6----------");

        System.out.println(ManipuladorMapas.obtenerClaves(mapaAnime));

        System.out.println(ManipuladorMapas.obtenerClaves(mapaCoches));

        //Ejercicio 7
        System.out.println("----------Ejercicio 7----------");

        System.out.println(ManipuladorMapas.actualizarValor(mapaAnime, "Naruto", "Boruto"));

        System.out.println(ManipuladorMapas.actualizarValor(mapaCoches,"Ford-T","Toyota"));

        //Ejercicio 8
        System.out.println("----------Ejercicio 8----------");

        System.out.println(ManipuladorMapas.fusionarMapas(mapaAnime,mapaCoches));

        //ejercicio 9
        System.out.println("----------Ejercicio 9----------");

        System.out.println(ManipuladorMapas.eliminarClavesNulas(mapaNull));

    }
}
