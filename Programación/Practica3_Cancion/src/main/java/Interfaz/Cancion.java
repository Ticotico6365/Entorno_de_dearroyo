package Interfaz;

import Clases.FechaImpl;

public interface Cancion {
    // getters
    String getNombre();
    String getInterprete();
    Integer getDuracion();
    FechaImpl getFechaDeLanzamiento();
    String getGenero();
    Integer getNumeroDeReproducciones();
    Double getCalificacion();
    Boolean getReproducir();

    //setters
    void setNumeroDeReproducciones(Integer numeroDeReproducciones);
    void setCalificacion(Double calificacion);
    void setReproducir(Boolean reproducir);
}
