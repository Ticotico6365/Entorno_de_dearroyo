import enumenadores.TipoProducto;
import modelos.*;
import utilidades.UtilidadesCliente;
import utilidades.UtilidadesFactura;
import utilidades.UtilidadesProducto;

import java.sql.ClientInfoStatus;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class pruebaV2 {
    public static void main(String[] args) {
        // PRuebas de utilidades facturas

        Almacen almacen = new Almacen(852,"Pedro",52);
        Producto producto1 = new Producto(1,1,"viena",LocalDate.of(2024,8,13), TipoProducto.ALIMENTACION,almacen,0.50);
        Producto producto2 = new Producto(2,2,"bollo",LocalDate.of(2024,8,13), TipoProducto.ALIMENTACION,almacen,0.50);
        Producto producto3 = new Producto(1,1,"Regañá",LocalDate.of(2024,8,13), TipoProducto.ALIMENTACION,almacen,0.50);
        Producto producto4 = new Producto(2,2,"Pepo",LocalDate.of(2024,8,13), TipoProducto.ALIMENTACION,almacen,0.50);

        Factura factura = new Factura(1,"F01",0.0,0.0,0.0,0.0, LocalDate.of(1789,5,7) ,LocalDate.of(2005,9,9),true, new ArrayList<>(), null);

        LineaFactura linea1 = new LineaFactura(1,factura,producto1,5);
        LineaFactura linea2 = new LineaFactura(1,factura,producto2,5);

        factura.setLineaFactura(List.of(linea1,linea2));


//        System.out.println("El importe total de la factura: " + UtilidadesFactura.calcularTotalAPagar(factura));
//
//        System.out.println("el importe base de la factura es: " + UtilidadesFactura.calcularBaseFactura(factura));
//
//        System.out.println(UtilidadesFactura.esFacturaVencida(factura));

        // Pruevas de Producto
        List<Producto> listaDeProductos = List.of(producto1,producto2,producto3, producto4);

        //ejercicio 1
        //System.out.println(UtilidadesProducto.getPorTipo(listaDeProductos,TipoProducto.ALIMENTACION));

        //ejercicio 2
//        List<Producto> productoList = UtilidadesProducto.getPorAlmacen(listaDeProductos, almacen);
//        for (Producto p : productoList ){
//            System.out.println(p.getDescripcion());
//        }

        //pruebas cliente
        //ejercicio 1
        Cliente cliente = new Cliente(1,"77871552S","David","Zamora Martínez",null, null);
        System.out.println(UtilidadesCliente.esDniValido(cliente));




    }




}
