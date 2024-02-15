package modelos;

import enumenadores.TipoCliente;

import java.util.Objects;

public class Cliente extends Persona{
    private TipoCliente tipoCliente;

    // getters -setters

    public TipoCliente getTipoCliente() {
        return tipoCliente;
    }

    public void setTipoCliente(TipoCliente tipoCliente) {
        this.tipoCliente = tipoCliente;
    }
    //constructores
        //vacio
    public Cliente() {
    }
        //completo
    public Cliente(Integer identificacion, String dni, String nombre, String apellidos, String direccion, TipoCliente tipoCliente) {
        super(identificacion,dni,nombre,apellidos,direccion);
        this.tipoCliente = tipoCliente;
    }
        //copia
    public Cliente(Cliente cliente){
        this.tipoCliente = cliente.getTipoCliente();
    }

    //metodos
    @Override
    public String toString() {
        return "Cliente{" +
                ", tipoCliente=" + tipoCliente +
                '}';
    }

    //equal y hashcode
        //equal
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Cliente cliente = (Cliente) o;
        return tipoCliente == cliente.tipoCliente;
    }

    //hashcode
    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), tipoCliente);
    }
}
