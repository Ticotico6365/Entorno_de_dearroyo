package Clases;

import Interfaces.PuntoEn3D;
import Interfaces.Segmento;

public class SegmentoImpl implements Segmento {
    private PuntoEn3D punto1;
    private PuntoEn3D punto2;

    // getters-setters
    public PuntoEn3D getPunto1() {
        return punto1;
    }

    public void setPunto1(PuntoEn3D punto1) {
        this.punto1 = punto1;
    }

    public PuntoEn3D getPunto2() {
        return punto2;
    }

    public void setPunto2(PuntoEn3D punto2) {
        this.punto2 = punto2;
    }

    public PuntoEn3D

    //constructores
        //vacio
    public SegmentoImpl() {
    }
        //completo
    public SegmentoImpl(PuntoEn3D punto1, PuntoEn3D punto2) {
        if (punto1 == null){
            this.punto1 = new PuntoEn3Dimpl(0D,0D,0D);
        }else if (punto2 == null){
            this.punto2 = new PuntoEn3Dimpl(0D,0D,0D);
        }else {
            this.punto1 = punto1;
            this.punto2 = punto2;
        }
    }
}
