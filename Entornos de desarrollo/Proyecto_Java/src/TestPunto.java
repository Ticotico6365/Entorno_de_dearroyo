package puntoplano;

public class TestPunto {
    public static void main(String[]args){
        //nombreInterfave nombre = new nombreClase();
        Punto p1= new PuntoImpl(4,6);

        System.out.println(p1);
        System.out.println("El valor de x es:"+p1.getX());
        System.out.println("El valor de y es: "+p1.getY());

        p1.setX(20);
        p1.setY(43);

        System.out.println("El valor nuevo de x es: "+p1.getX());
        System.out.println("El valor nuevo de y es: "+p1.getY());

    }

}
