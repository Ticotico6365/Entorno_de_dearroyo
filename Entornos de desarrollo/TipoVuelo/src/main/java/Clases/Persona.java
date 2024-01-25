package Clases;

public class Persona implements Interfaces.Persona{
    private String nombre;
    private String apellido1;
    private String apellido2;
    private String dni;
    private Integer edad;

    // cosrtuctores
    public Persona() {
    }
    public Persona(String nombre, String apellido1, String apellido2, String dni, Integer edad) {
        this.nombre = nombre;
        this.apellido1 = apellido1;
        this.apellido2 = apellido2;
        this.dni = dni;
        this.edad = edad;
    }

    // getters - setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido1() {
        return apellido1;
    }

    public void setApellido1(String apellido1) {
        this.apellido1 = apellido1;
    }

    public String getApellido2() {
        return apellido2;
    }

    public void setApellido2(String apellido2) {
        this.apellido2 = apellido2;
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

    public Integer getEdad() {
        return edad;
    }

    public void setEdad(Integer edad) {
        this.edad = edad;
    }

    // toString
    public String toString() {
        return getNombre() + " " + getApellido1() + " " + getApellido2() + " " + "," + getDni() + "," + getEdad() + "años";
    }

}

