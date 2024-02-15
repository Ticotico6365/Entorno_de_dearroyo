package Clases;

import Interfaz.Fecha;

public class Cancion implements Interfaz.Cancion {
    private String nombre;
    private String interprete;
    private Integer duracion;
    private FechaImpl fechaDeLanzamiento;
    private String genero;
    private Integer numeroDeReproducciones;
    private Double calificacion;
    private Boolean reproducir;

    // getter-setters
    public String getNombre() {
        return nombre;
    }

    public String getInterprete() {
        return interprete;
    }

    public Integer getDuracion() {
        return duracion;
    }

    public FechaImpl getFechaDeLanzamiento() {
        return fechaDeLanzamiento;
    }

    public String getGenero() {
        return genero;
    }

    public Integer getNumeroDeReproducciones() {
        return numeroDeReproducciones;
    }

    public void setNumeroDeReproducciones(Integer numeroDeReproducciones) {
        this.numeroDeReproducciones = numeroDeReproducciones;
    }

    public Double getCalificacion() {
        return calificacion;
    }

    public void setCalificacion(Double calificacion) {
        this.calificacion = calificacion;
    }

    public Boolean getReproducir() {
        return reproducir;
    }

    public void setReproducir(Boolean reproducir) {
        this.reproducir = reproducir;
    }

    //constructores
        //vacio
    public Cancion() {
    }
        //completo
    public Cancion(String nombre, String interprete, Integer duracion, Fecha fechaDeLanzamiento, String genero, Integer numeroDeReproducciones, Double calificacion, Boolean reproducir) {
        this.nombre = nombre;
        this.interprete = interprete;
        this.duracion = duracion;
        this.fechaDeLanzamiento = (FechaImpl) fechaDeLanzamiento;
        this.genero = genero;
        this.numeroDeReproducciones = numeroDeReproducciones;
        if (0 > calificacion){
            this.calificacion = 0D;
        }if (calificacion > 10) {
            this.calificacion = 10D;
        }if (0 <= calificacion && calificacion >= 10){
            this.calificacion = calificacion;
        }
        this.reproducir = reproducir;
    }

        //copia
    public Cancion(Cancion cancion){
        this.nombre = cancion.getNombre();
        this.interprete = cancion.getInterprete();
        this.duracion = cancion.getDuracion();
        this.fechaDeLanzamiento = cancion.getFechaDeLanzamiento();
        this.genero = cancion.getGenero();
        this.numeroDeReproducciones = cancion.getNumeroDeReproducciones();
        this.calificacion = cancion.getCalificacion();
        this.reproducir = cancion.getReproducir();
    }

    //toString
    public String toString() {
        return "[" + nombre + ", " + interprete + "]";
    }
}
