package modelos;

import java.util.Objects;

public class Persona {
    private Integer indentificador;
    private String dni;
    private String nombre;
    private String apellidos;
    private String direccion;

    //getters -setters

    public Integer getIndentificador() {
        return indentificador;
    }

    public void setIndentificador(Integer indentificador) {
        this.indentificador = indentificador;
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    //constructores
        //vacio

    public Persona() {
    }
        //completo

    public Persona(Integer indentificador, String dni, String nombre, String apellidos, String direccion) {
        this.indentificador = indentificador;
        this.dni = dni;
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.direccion = direccion;
    }
        //copia
    public Persona(Persona persona) {
        this.indentificador = persona.getIndentificador();
        this.dni = persona.getDni();
        this.nombre = persona.getNombre();
        this.apellidos = persona.getApellidos();
        this.direccion = persona.getDireccion();
    }

    //equals y hashcode

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Persona persona = (Persona) o;
        return Objects.equals(indentificador, persona.indentificador) && Objects.equals(dni, persona.dni) && Objects.equals(nombre, persona.nombre) && Objects.equals(apellidos, persona.apellidos) && Objects.equals(direccion, persona.direccion);
    }

    @Override
    public int hashCode() {
        return Objects.hash(indentificador, dni, nombre, apellidos, direccion);
    }


    //toString

    @Override
    public String toString() {
        return "Persona{" +
                "indentificador=" + indentificador +
                ", dni='" + dni + '\'' +
                ", nombre='" + nombre + '\'' +
                ", apellidos='" + apellidos + '\'' +
                ", direccion='" + direccion + '\'' +
                '}';
    }
}
