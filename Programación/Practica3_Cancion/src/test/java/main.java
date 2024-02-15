import Clases.FechaImpl;
import Interfaz.Cancion;
import Interfaz.Fecha;

public class main {
    public static void main(String[] args) {
        Fecha fecha = new FechaImpl(7,7,2006);
        Cancion cancion = new Clases.Cancion("Awareness", "MoonDeity", 500, fecha,"Phonk",85,-90.0, true);

        System.out.println(cancion);
        System.out.println(cancion.getCalificacion());

        System.out.println(fecha);
    }
}
