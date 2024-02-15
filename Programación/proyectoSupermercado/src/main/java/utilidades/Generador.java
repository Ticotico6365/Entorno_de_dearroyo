package utilidades;

import com.github.javafaker.Faker;
import enumenadores.TipoContrato;
import enumenadores.TipoEmpresa;
import modelos.*;

import java.util.ArrayList;
import java.util.List;

public class Generador {
    //Personas
    public static Persona crearPersona(){
        //iniciamos la variable Faker
        Faker faker = new Faker();

        Persona persona = new Persona();
        persona.setIndentificador(faker.number().randomDigitNotZero());
        persona.setDni(faker.number().numberBetween(10000000, 99999999) + faker.letterify("?").toUpperCase());
        persona.setNombre(faker.name().firstName());
        persona.setApellidos(faker.name().lastName());
        persona.setDireccion(faker.address().fullAddress());
        return persona;
    }
        //Empresa
    public static Empresa crearEmpresa(int numEmpleados){
        Faker faker = new Faker();

        Empresa empresa = new Empresa();
        empresa.setEmpleados(crearEmpleados(numEmpleados));
        empresa.setIdentificador(faker.number().randomDigitNotZero());
        empresa.setCodigoEmpresa(faker.company().logo());
        empresa.setTipoEmpresa(TipoEmpresa.values()[faker.number().numberBetween(0, TipoEmpresa.values().length - 1)]);

        return empresa;
    }

    public static List<Empresa> crearEmpresas (int numEmpleados, int numEmpresas){
        List<Empresa> empresas = new ArrayList<>();

        for (int i = 0; i < numEmpresas; i++) {
            empresas.add(crearEmpresa(numEmpleados));
        }
        return empresas;
    }

        //Empleado
    public static Empleado crearEmpleado(){
        Faker faker = new Faker();

        Empleado empleado = new Empleado(crearPersona());
        empleado.setNumTelefono(String.valueOf(faker.number().numberBetween(600000000, 6999999)));
        empleado.setEmpresa(crearEmpresa(faker.number().randomDigitNotZero()));
        empleado.setContrato(crearContrato());
        return empleado;
    }

    public static List<Empleado> crearEmpleados(int numEmpleados){
        List<Empleado> empleados = new ArrayList<>();

        for (int i = 0 ; i<numEmpleados ; i++){
            empleados.add(crearEmpleado());
        }

        return empleados;
    }

    // Contrato
    public static Contrato crearContrato (){
        Faker faker = new Faker();

        Contrato contrato = new Contrato();
        contrato.setTipoContrato(TipoContrato.values()[faker.number().numberBetween(0, TipoContrato.values().length - 1)]);
        contrato.setIdentificador(faker.number().randomDigitNotZero());
        contrato.setSalarioBase(faker.number().randomDouble(2, 1080,3000));

        return contrato;
    }

    // Almacén
    public static Almacen crearAlmacen (){
        Faker faker = new Faker();

        Almacen almacen = new Almacen();
        almacen.setCapacidad(faker.number().numberBetween(1000, 10000));
        almacen.setIdentificador(faker.number().randomDigitNotZero());
        almacen.setNombre(faker.company().name());

        return almacen;
    }

    public static void main(String[] args) {
        System.out.println(crearPersona());
    }
}
