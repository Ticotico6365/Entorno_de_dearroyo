package Clases;

import Interfaces.PuntoEn3D;

public class PuntoEn3Dimpl implements PuntoEn3D {
    private Double x;
    private Double y;
    private Double z;

    //getters-setters
    public Double getX() {
        return x;
    }

    public void setX(Double x) {
        this.x = x;
    }

    public Double getY() {
        return y;
    }

    public void setY(Double y) {
        this.y = y;
    }

    public Double getZ() {
        return z;
    }

    public void setZ(Double z) {
        this.z = z;
    }

    public Double getDistanciaPuntos (PuntoEn3D puntoEn3D1, PuntoEn3D puntEn3D2){
        PuntoEn3D vectorV = puntoEn3D1.getX() - punto

        return Math.sqrt(Math.pow(puntoEn3D1.getX(), 2D) + Math.pow(puntoEn3D1.getY(), 2D) + Math.pow(puntoEn3D1.getZ(), 2D));
    }
    //constructores
        //vacio
    public PuntoEn3Dimpl() {
    }

    //completo
    public PuntoEn3Dimpl(Double x, Double y, Double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
}
