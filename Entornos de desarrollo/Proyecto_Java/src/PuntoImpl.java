package puntoplano;

public class PuntoImpl  implements Punto{
    //1º genero variables
    private Integer x;
    private Integer y;

    //2º constructor
    public PuntoImpl(Integer x1, Integer y1){
        x=x1;
        y=y1;
    }

    //3º métodos
    //métodos constructores
    public Integer getX(){

        return x;
    }
    public Integer getY(){
        return y;
    }
    //métodos modificables
    public void setX(Integer x1){
        x=x1;
    }
    public void setY(Integer y1){
        y=y1;
    }

    public String toString(){
        String s= "("+getX()+","+getY()+")";
        return s;
    }
}
