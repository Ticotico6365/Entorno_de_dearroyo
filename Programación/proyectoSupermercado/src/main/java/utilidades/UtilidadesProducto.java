package utilidades;

import enumenadores.TipoProducto;
import modelos.Almacen;
import modelos.Producto;

import java.util.ArrayList;
import java.util.List;

public class UtilidadesProducto {
    public static List<Producto> getPorTipo(List<Producto> productos, TipoProducto tipo){
        List<Producto> productoDelTipo = new ArrayList<>();
        for (Producto producto : productos){
            if (producto.getTipoProducto().equals(tipo)){
                productoDelTipo.add(producto);
            }
        }
        return productoDelTipo;
    }

    public static List<Producto> getPorAlmacen(List<Producto> productos, Almacen almacen){
        List<Producto> productoFinal = new ArrayList<>();

        for(Producto p : productos){
            if( p == null && p.getAlmacen().equals(almacen)){
                productoFinal.add(p);
            }
        }
        return productoFinal;
    }
}
