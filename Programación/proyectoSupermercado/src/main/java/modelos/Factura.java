package modelos;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Factura {
    private Integer identificador;
    private String codigoFactura;
    private Double importeFactura;
    private Double descuento;
    private Double iva;
    private Double totalAPagar;
    private LocalDate fechaDeEmision;
    private LocalDate fechaDeVencimiento;
    private Boolean pagada;
    private List<LineaFactura> lineaFactura;
    private Cliente cliente;

    //getters-setters
    public Integer getIdentificador() {
        return identificador;
    }

    public void setIdentificador(Integer identificador) {
        this.identificador = identificador;
    }

    public String getCodigoFactura() {
        return codigoFactura;
    }

    public void setCodigoFactura(String codigoFactura) {
        this.codigoFactura = codigoFactura;
    }

    public Double getImporteFactura() {
        return importeFactura;
    }

    public void setImporteFactura(Double importeFactura) {
        this.importeFactura = importeFactura;
    }

    public Double getDescuento() {
        return descuento;
    }

    public void setDescuento(Double descuento) {
        this.descuento = descuento;
    }

    public Double getIva() {
        return iva;
    }

    public void setIva(Double iva) {
        this.iva = iva;
    }

    public Double getTotalAPagar() {
        return totalAPagar;
    }

    public void setTotalAPagar(Double totalAPagar) {
        this.totalAPagar = totalAPagar;
    }

    public LocalDate getFechaDeEmision() {
        return fechaDeEmision;
    }

    public void setFechaDeEmision(LocalDate fechaDeEmision) {
        this.fechaDeEmision = fechaDeEmision;
    }

    public LocalDate getFechaDeVencimiento() {
        return fechaDeVencimiento;
    }

    public void setFechaDeVencimiento(LocalDate fechaDeVencimiento) {
        this.fechaDeVencimiento = fechaDeVencimiento;
    }

    public Boolean getPagada() {
        return pagada;
    }

    public void setPagada(Boolean pagada) {
        this.pagada = pagada;
    }

    public List<LineaFactura> getLineaFactura() {
        return lineaFactura;
    }

    public void setLineaFactura(List<LineaFactura> lineaFactura) {
        this.lineaFactura = lineaFactura;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    //constructores
        //vacio
    public Factura() {
    }

        //completo
    public Factura(Integer identificador, String codigoFactura, Double importeFactura, Double descuento, Double iva, Double totalAPagar, LocalDate fechaDeEmision, LocalDate fechaDeVencimiento, Boolean pagada, List<LineaFactura> lineaFactura, Cliente cliente) {
        this.identificador = identificador;
        this.codigoFactura = codigoFactura;
        this.importeFactura = importeFactura;
        this.descuento = descuento;
        this.iva = iva;
        this.totalAPagar = totalAPagar;
        this.fechaDeEmision = fechaDeEmision;
        this.fechaDeVencimiento = fechaDeVencimiento;
        this.pagada = pagada;
        this.lineaFactura = lineaFactura;
        this.cliente = cliente;
    }
        //copia
    public Factura(Factura factura){
        this.identificador = factura.getIdentificador();
        this.codigoFactura = factura.getCodigoFactura();
        this.importeFactura = factura.getImporteFactura();
        this.descuento = factura.getDescuento();
        this.iva = factura.getIva();
        this.totalAPagar = factura.getTotalAPagar();
        this.fechaDeEmision = factura.getFechaDeEmision();
        this.fechaDeVencimiento = factura.getFechaDeVencimiento();
        this.pagada = factura.getPagada();
        this.lineaFactura = factura.getLineaFactura();
        this.cliente = factura.getCliente();
    }

    //equal y hashcode
        //equal
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Factura factura = (Factura) o;
        return Objects.equals(identificador, factura.identificador) && Objects.equals(codigoFactura, factura.codigoFactura) && Objects.equals(importeFactura, factura.importeFactura) && Objects.equals(descuento, factura.descuento) && Objects.equals(iva, factura.iva) && Objects.equals(totalAPagar, factura.totalAPagar) && Objects.equals(fechaDeEmision, factura.fechaDeEmision) && Objects.equals(fechaDeVencimiento, factura.fechaDeVencimiento) && Objects.equals(pagada, factura.pagada) && Objects.equals(lineaFactura, factura.lineaFactura) && Objects.equals(cliente, factura.cliente);
    }
        //hashcode
    @Override
    public int hashCode() {
        return Objects.hash(identificador, codigoFactura, importeFactura, descuento, iva, totalAPagar, fechaDeEmision, fechaDeVencimiento, pagada, lineaFactura, cliente);
    }

    // toString

    @Override
    public String toString() {
        return "Factura{" +
                "identificador=" + identificador +
                ", codigoFactura='" + codigoFactura + '\'' +
                ", importeFactura=" + importeFactura +
                ", descuento=" + descuento +
                ", iva=" + iva +
                ", totalAPagar=" + totalAPagar +
                ", fechaDeEmision=" + fechaDeEmision +
                ", fechaDeVencimiento=" + fechaDeVencimiento +
                ", pagada=" + pagada +
                ", lineaFactura=" + lineaFactura +
                ", cliente=" + cliente +
                '}';
    }
}
