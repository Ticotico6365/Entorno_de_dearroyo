package Clases;

public class Vuelo implements Interfaces.Vuelo {
    private String codigoVuelo;
    private String destino;
    private Double precio;
    private Integer numeroDePlazas;
    private Integer nuemroDePasajeros;
    private Fecha fechaDeSalida;
    private Persona piloto;

    // constructores
    public Vuelo() {
    }

    public Vuelo(String codigoVuelo, String destino, Double precio, Integer numeroDePlazas, Integer nuemroDePasajeros, Fecha fechaDeSalida, Persona piloto) {
        this.codigoVuelo = codigoVuelo;
        this.destino = destino;
        this.precio = precio;
        this.numeroDePlazas = numeroDePlazas;
        this.nuemroDePasajeros = nuemroDePasajeros;
        this.fechaDeSalida = fechaDeSalida;
        this.piloto = piloto;
    }

    public Vuelo(Double precio, Integer nuemroDePasajeros) {
        this.precio = precio;
        this.nuemroDePasajeros = nuemroDePasajeros;
    }
    // getters - setters

    public String getCodigoVuelo() {
        return codigoVuelo;
    }

    public String getDestino() {
        return destino;
    }

    public Double getPrecio() {
        return precio;
    }

    public void setPrecio(Double precio) {
        this.precio = precio;
    }

    public Integer getNumeroDePlazas() {
        return numeroDePlazas;
    }

    public Integer getNuemroDePasajeros() {
        return nuemroDePasajeros;
    }

    public void setNuemroDePasajeros(Integer nuemroDePasajeros) {
        this.nuemroDePasajeros = nuemroDePasajeros;
    }

    public Fecha getFechaDeSalida() {
        return fechaDeSalida;
    }

    public Persona getPiloto() {
        return piloto;
    }

    public void setPiloto(Persona piloto) {
        this.piloto = piloto;
    }

    // recaudación
    public Double recaudacion(){
        return getPrecio()*getNuemroDePasajeros();
    }

    // toString
    public String toString(){
        return getCodigoVuelo()+"("+ getDestino()+")"+getPiloto()+"-"+getFechaDeSalida();
    }
}
