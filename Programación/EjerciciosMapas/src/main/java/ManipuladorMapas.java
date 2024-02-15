import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class ManipuladorMapas {
    //Ejercicio 1
    public static Map<String,String> agregarElemento (Map<String, String> mapa, String key, String value){
        //metemos el elemento y la clave
        mapa.put(key, value);
        //devolvemos el mapa con el elemento nuevo
        return mapa;
    }

    //Ejercicio 2
    public static Map<String,String> eliminarElemento (Map<String, String> mapa, String key){
        mapa.remove(key);
        return mapa;
    }

    //ejercicio 3
    public static String obtenerElemento (Map<String, String> mapa, String key){
        return mapa.get(key);
    }

    //ejercicio 4
    public static Integer contarElementos (Map<String, String> mapa){
        return mapa.size();
    }

    //ejercicio 5
    public static Boolean verificarExistenciaClave (Map<String, String> mapa, String key){
        return mapa.containsKey(key);
    }

    //ejercicio 6
    public static Set<String> obtenerClaves (Map<String, String> mapa){
        return mapa.keySet();
    }

    //ejercicio 7
    public static Map<String, String> actualizarValor(Map<String,String> mapa, String key, String newValue){
        mapa.remove(key);
        mapa.put(key,newValue);
        return mapa;
    }

    //ejercicio 8
    public static Map<String, String> fusionarMapas (Map<String,String> mapa1, Map<String,String> mapa2){
        //metemos el mapa2 en el mapa final y luego los elementos del mapa1 se meten uno por uno en el mapa final
        Map<String, String> mapaFinal = new HashMap<>(mapa2);
        Set<String> elementosMapa1 = obtenerClaves(mapa1);
        for (String i: elementosMapa1) {
            mapaFinal.put(i, mapa1.get(i));
        }
        return mapaFinal;
    }

    //ejercicio 9
    public static Map<String,String> eliminarClavesNulas (Map<String,String> mapa){
        Map<String,String> mapaFinal = new HashMap<>();
        Set<String> elementosmapa = obtenerClaves(mapa);
        for(String i : elementosmapa){
            if (i != null){
                mapaFinal.put(i,mapa.get(i));
            }
        }
        return mapaFinal;
    }
}
