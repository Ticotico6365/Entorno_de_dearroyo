package modelos;

import java.util.Objects;

public class LineaFactura {
    private Integer codigo;
    private Factura factura;
    private Producto producto;
    private Integer cantidad;

    //getters-setters
    public Integer getCodigo() {
        return codigo;
    }

    public void setCodigo(Integer codigo) {
        this.codigo = codigo;
    }

    public Factura getFactura() {
        return factura;
    }

    public void setFactura(Factura factura) {
        this.factura = factura;
    }

    public Producto getProducto() {
        return producto;
    }

    public void setProducto(Producto producto) {
        this.producto = producto;
    }

    public Integer getCantidad() {
        return cantidad;
    }

    public void setCantidad(Integer cantidad) {
        this.cantidad = cantidad;
    }

    //constructores
        //vacio
    public LineaFactura() {
    }
        //completo
    public LineaFactura(Integer codigo, Factura factura, Producto producto, Integer cantidad) {
        this.codigo = codigo;
        this.factura = factura;
        this.producto = producto;
        this.cantidad = cantidad;
    }
        //copia
    public LineaFactura(LineaFactura lineaFactura){
        this.codigo = lineaFactura.getCodigo();
        this.factura = lineaFactura.getFactura();
        this.producto = lineaFactura.getProducto();
        this.cantidad = lineaFactura.getCantidad();
    }

    //equal y hashcode
        //equal
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        LineaFactura that = (LineaFactura) o;
        return Objects.equals(codigo, that.codigo) && Objects.equals(factura, that.factura) && Objects.equals(producto, that.producto) && Objects.equals(cantidad, that.cantidad);
    }
        //hashcode
    @Override
    public int hashCode() {
        return Objects.hash(codigo, factura, producto, cantidad);
    }
}
