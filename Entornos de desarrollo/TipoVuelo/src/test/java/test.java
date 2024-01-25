import Interfaces.Fecha;
import Interfaces.Persona;
import Interfaces.Vuelo;

public class test {
    public static void main(String[] args) {
        Fecha fecha = new Clases.Fecha(9,9,2005);
        Persona piloto = new Clases.Persona("Juan","Pérez", "Machado", "89745S",40);
        Vuelo vuelo = new Clases.Vuelo("75543354354sv","mi casa", 78.9, 789,96,fecha,piloto);
    }
}
