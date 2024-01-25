package Interfaces;

import Clases.Fecha;
import Clases.Persona;

public interface Vuelo {
    // getter
    String getCodigoVuelo();
    String getDestino();
    Double getPrecio();
    Integer getNumeroDePlazas();
    Integer getNuemroDePasajeros();
    Fecha getFechaDeSalida();
    Persona getPiloto();

    // setters
    void setPrecio(Double precio);
    void setPiloto(Persona piloto);

    // recaudación
    Double recaudacion();
}
