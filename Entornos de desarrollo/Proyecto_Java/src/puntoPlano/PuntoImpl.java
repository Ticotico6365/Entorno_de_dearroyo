package puntoPlano;

import puntoPlano.Punto;

public class PuntoImpl implements Punto {
    //1º.-Creamos nuestras variables
    private Double x;
    private Double y;

    //2º.-Cronstructor
    public PuntoImpl(Double xn, Double yn){
        x = xn;
        y = yn;
    }
    //3º.-getters y setters
    public Double getX(){
        return x;
    }
    public void setX(Double x1){
        x = x1;
    }
    public Double getY(){
        return y;
    }
    public void setY(Double y1){
        y = y1;
    }
    //4º.-toString
    public String toString(){
        String r = "(" + getX() + "," + getY() + ")";
        return r;
    }
    //5º.-métodos
    public static Double DistanciaA2pts(Punto p){
        Double a1 = Math.pow(p.getX()-getX(), 2);
        Double b1 = Math.pow(p.getY()-getY(), 2);
        Double resultado = Math.sqrt(a1 + b1);
        return resultado;
    }
}
