package modelos;

import java.util.Objects;

public class Empleado extends Persona {
    private String numTelefono;
    private Empresa empresa;
    private Contrato Contrato;

    // getter-setters
    public String getNumTelefono() {
        return numTelefono;
    }

    public void setNumTelefono(String numTelefono) {
        this.numTelefono = numTelefono;
    }

    public Empresa getEmpresa() {
        return empresa;
    }

    public void setEmpresa(Empresa empresa) {
        this.empresa = empresa;
    }

    public modelos.Contrato getContrato() {
        return Contrato;
    }

    public void setContrato(modelos.Contrato contrato) {
        Contrato = contrato;
    }

    //constructores
        //vacio
    public Empleado() {
    }
        //completo
    public Empleado(Integer indentificador, String dni, String nombre, String apellidos, String direccion, String numTelefono, Empresa empresa, modelos.Contrato contrato) {
        super(indentificador,dni,nombre,apellidos,direccion);
        this.numTelefono = numTelefono;
        this.empresa = empresa;
        Contrato = contrato;
    }
        //copia
    public Empleado(Empleado empleado){
        this.numTelefono = empleado.getNumTelefono();
        this.empresa = empleado.getEmpresa();
        Contrato = empleado.getContrato();
    }

    public Empleado(Persona persona){
        this.setIndentificador(persona.getIndentificador());
        this.setDni(persona.getDni());
        this.setNombre(persona.getNombre());
        this.setApellidos(persona.getApellidos());
        this.setDireccion(persona.getDireccion());
    }

    //toString

    @Override
    public String toString() {
        return "Empleado{" +
                ", numTelefono='" + numTelefono + '\'' +
                ", empresa=" + empresa +
                ", Contrato=" + Contrato +
                '}';
    }

    //equal y hashcode
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Empleado empleado = (Empleado) o;
        return Objects.equals(numTelefono, empleado.numTelefono) && Objects.equals(empresa, empleado.empresa) && Objects.equals(Contrato, empleado.Contrato);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), numTelefono, empresa, Contrato);
    }
}
