package modelos;

import enumenadores.TipoProducto;

import java.time.LocalDate;
import java.util.Objects;

public class Producto {
    private Integer identificador;
    private Integer codigo;
    private String descripcion;
    private LocalDate fechaCaducidad;
    private TipoProducto tipoProducto;
    private Almacen almacen;
    private Double precio;

    // GETTERS - SETTERS

    public Integer getIdentificador() {
        return identificador;
    }

    public void setIdentificador(Integer identificador) {
        this.identificador = identificador;
    }

    public Integer getCodigo() {
        return codigo;
    }

    public void setCodigo(Integer codigo) {
        this.codigo = codigo;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public LocalDate getFechaCaducidad() {
        return fechaCaducidad;
    }

    public void setFechaCaducidad(LocalDate fechaCaducidad) {
        this.fechaCaducidad = fechaCaducidad;
    }

    public TipoProducto getTipoProducto() {
        return tipoProducto;
    }

    public void setTipoProducto(TipoProducto tipoProducto) {
        this.tipoProducto = tipoProducto;
    }

    public Almacen getAlmacen() {
        return almacen;
    }

    public void setAlmacen(Almacen almacen) {
        this.almacen = almacen;
    }

    public Double getPrecio() {
        return precio;
    }

    public void setPrecio(Double precio) {
        this.precio = precio;
    }

    //constructores
    //completo
    public Producto(Integer identificador, Integer codigo, String descripcion, LocalDate fechaCaducidad, TipoProducto tipoProducto, Almacen almacen, Double precio) {
        this.identificador = identificador;
        this.codigo = codigo;
        this.descripcion = descripcion;
        this.fechaCaducidad = fechaCaducidad;
        this.tipoProducto = tipoProducto;
        this.almacen = almacen;
        this.precio = precio;
    }
        //copia
    public Producto(Producto Producto){
        this.identificador = Producto.getIdentificador();
        this.codigo = Producto.getCodigo();
        this.descripcion = Producto.getDescripcion();
        this.fechaCaducidad = Producto.getFechaCaducidad();
        this.tipoProducto = Producto.getTipoProducto();
        this.almacen = Producto.getAlmacen();
        this.precio = Producto.getPrecio();
    }
        //vacio
    public Producto() {
    }


    // metodos

    @Override
    public String toString() {
        return "Producto{" +
                "identificador=" + identificador +
                ", codigo=" + codigo +
                ", descripcion='" + descripcion + '\'' +
                ", fechaCaducidad=" + fechaCaducidad +
                ", tipoProducto=" + tipoProducto +
                ", almacen=" + almacen +
                ", precio=" + precio +
                '}';
    }

    //equal y hashcode
        //equal
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Producto producto = (Producto) o;
        return Objects.equals(identificador, producto.identificador) && Objects.equals(codigo, producto.codigo) && Objects.equals(descripcion, producto.descripcion) && Objects.equals(fechaCaducidad, producto.fechaCaducidad) && tipoProducto == producto.tipoProducto && Objects.equals(almacen, producto.almacen) && Objects.equals(precio, producto.precio);
    }
        //hashcode
    @Override
    public int hashCode() {
        return Objects.hash(identificador, codigo, descripcion, fechaCaducidad, tipoProducto, almacen, precio);
    }
}
