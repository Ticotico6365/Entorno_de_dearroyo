package puntoPlano;

import puntoPlano.Punto;
import puntoPlano.PuntoImpl;

public class Test {
    public static void main(String[] args) {
        //nombreInterface n = new nombreClase(parametros);
        Punto p = new PuntoImpl(5.1,2.4);
        System.out.println(p);
        System.out.println("El valor de x: " + p.getX() + "\n"); // el \n es el salto de carro, que es vásicamente un enter
        p.setY(3.3);
        System.out.println(p);

        Punto p2 = new PuntoImpl(9.0, 1.0);
    }
}
