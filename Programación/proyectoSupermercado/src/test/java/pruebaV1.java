import enumenadores.TipoCliente;
import enumenadores.TipoProducto;
import modelos.Almacen;
import modelos.Cliente;
import modelos.Producto;

import java.time.LocalDate;

public class pruebaV1 {
    public static void main(String[] args) {

        //almacen
        Almacen almacen = new Almacen(5648,"Machados",98);
        System.out.println(almacen);

        //cliente
        Cliente cliente = new Cliente(78954,"77871552D","Peppe","Fgueros","callle lumbreras 3", TipoCliente.PARTICULAR);
        System.out.println(cliente);

        //producto
        Producto producto = new Producto(789,963,"Mu bonito", LocalDate.now(),TipoProducto.DROGUERIA,almacen,78.9);
        System.out.println(producto);


    }
}
