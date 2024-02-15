package utilidades;

import modelos.Almacen;
import modelos.Producto;

import java.util.ArrayList;
import java.util.List;

public class UtilidadesAlmacen {
    public boolean validarAlmacenes(List<Producto> productos){
        List<Almacen> almacenes = new ArrayList<>();
        for (Producto i : productos){
            almacenes.add(i.getAlmacen());
        }
        for (Producto i : productos){
            if (i.getAlmacen().getCapacidad() == almacenes.get(almacenes.indexOf(i.getAlmacen())).getCapacidad()){
                return true;
            }
        }
    }
}
