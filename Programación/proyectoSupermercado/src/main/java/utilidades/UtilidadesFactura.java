package utilidades;

import modelos.Cliente;
import modelos.Factura;
import modelos.LineaFactura;

import java.time.LocalDate;
import java.util.List;
import java.util.Objects;

public class UtilidadesFactura {
    //a
    public static Boolean esFacturaVencida(Factura factura){
        return factura.getFechaDeVencimiento().isAfter(LocalDate.now()) || factura.getFechaDeVencimiento().equals(LocalDate.now());
    }
    //b
    public static Double calcularBaseFactura(Factura factura){
        List<LineaFactura> lineaFactura = factura.getLineaFactura();
        double total = 0.0;
        for(LineaFactura linea : lineaFactura){
            total = total + linea.getProducto().getPrecio() * linea.getCantidad();
        }
        return total;
    }
    //c
    public static Double calcularTotalAPagar(Factura factura){
        return (factura.getImporteFactura() - factura.getDescuento()) * factura.getIva();
    }

    //V5

    public Double gastoTotalCliente(List<Factura> facturas, Cliente cliente){
        double total = 0D;
        for (Factura i : facturas){
            if (i.getCliente().equals(cliente)){
                total += i.getTotalAPagar();
            }
        }
        return total;
    }

    public Double totalFacturadoPeriodo(List<Factura> facturas, LocalDate fechaInicio, LocalDate fechaFin){
        Double total = 0D;

        for (Factura i : facturas){
            if (i.getFechaDeEmision().isAfter(fechaInicio) && i.getFechaDeVencimiento().isBefore(fechaFin)){
                total += i.getTotalAPagar();
            }
        }
        return total;
    }



}
