package Clases;

public class Fecha implements Interfaces.Fecha{
    private Integer dia;
    private Integer mes;
    private Integer anyo;

    // constructores
    public Fecha() {
    }

    public Fecha(Integer dia, Integer mes, Integer anyo) {
        this.dia = dia;
        this.mes = mes;
        this.anyo = anyo;
    }

    // getters - setters
    public Integer getDia() {
        return dia;
    }

    public void setDia(Integer dia) {
        this.dia = dia;
    }

    public Integer getMes() {
        return mes;
    }

    public void setMes(Integer mes) {
        this.mes = mes;
    }

    public Integer getAnyo() {
        return anyo;
    }

    public void setAnyo(Integer anyo) {
        this.anyo = anyo;
    }

    // toString
    public String toString() {
        return getDia() + "/" + getMes() + "/" + getAnyo();
    }
}
