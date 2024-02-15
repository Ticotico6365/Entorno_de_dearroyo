import enumenadores.TipoContrato;
import enumenadores.TipoEmpresa;
import modelos.Contrato;
import modelos.Empleado;
import modelos.Empresa;
import utilidades.UltilidadesEmpresa;
import utilidades.UtidadesContrato;
import utilidades.UtilidadesEmpleado;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class pruebaV4 {
    public static void main(String[] args) {

        //contratos
        Contrato contrato1 = new Contrato(1,1500D, TipoContrato.INDEFINIDO);
        Contrato contrato2 = new Contrato(2,1300D, TipoContrato.OBRAYSERVICIO);
        Contrato contrato3 = new Contrato(3,2000D, TipoContrato.OBRAYSERVICIO);
        Contrato contrato4 = new Contrato(4,2100D, TipoContrato.OBRAYSERVICIO);
        Contrato contrato5 = new Contrato(5,1400D, TipoContrato.PRACTICAS);
        Contrato contrato6 = new Contrato(6,1300D, TipoContrato.INDEFINIDO);
        Contrato contrato7 = new Contrato(7,1600D, TipoContrato.PRACTICAS);
        Contrato contrato8 = new Contrato(8, 2500D, TipoContrato.INDEFINIDO);
        Contrato contrato9 = new Contrato(9, 1080D, TipoContrato.OBRAYSERVICIO);
        Contrato contrato10 = new Contrato(10, 1080D, TipoContrato.OBRAYSERVICIO);
        Contrato contrato11 = new Contrato(11, 2100D, TipoContrato.OBRAYSERVICIO);
        Contrato contrato12 = new Contrato(12, 1110D, TipoContrato.PRACTICAS);
        Contrato contrato13 = new Contrato(13, 1999D, TipoContrato.INDEFINIDO);
        Contrato contrato14 = new Contrato(14, 1600D, TipoContrato.PRACTICAS);
        Contrato contrato15 = new Contrato(15, 1600D, TipoContrato.INDEFINIDO);
        Contrato contrato16 = new Contrato(16, 1200D, TipoContrato.OBRAYSERVICIO);
        Contrato contrato17 = new Contrato(17, 2500D, TipoContrato.OBRAYSERVICIO);
        Contrato contrato18 = new Contrato(18, 2200D, TipoContrato.OBRAYSERVICIO);
        Contrato contrato19 = new Contrato(19, 1300D, TipoContrato.PRACTICAS);
        Contrato contrato20 = new Contrato(20, 1400D, TipoContrato.INDEFINIDO);
        Contrato contrato21 = new Contrato(21, 1700D, TipoContrato.PRACTICAS);
        Contrato contrato22 = new Contrato(22, 1800D, TipoContrato.INDEFINIDO);


        List<Contrato> contratos = new ArrayList<>(List.of(contrato1,contrato2,contrato3,contrato4,contrato5,contrato6, contrato7,contrato8,contrato9,contrato10,contrato11,contrato12,contrato13,contrato14,contrato15,contrato16,contrato17,contrato18,contrato19,contrato20,contrato21,contrato22));

//        System.out.println( UtidadesContrato.getSalarioMedioTipoContrato(contratos));
//
//        System.out.println(UtidadesContrato.getNumContratosPorTipo(contratos));
//
//        System.out.println(UtidadesContrato.getListContratosPorTipo(contratos));

        //Emperesa
        List<Empleado> empleadosEmpresa1 = new ArrayList<>();
        List<Empleado> empleadosEmpresa2 = new ArrayList<>();
        List<Empleado> empleadosEmpresa3 = new ArrayList<>();
        List<Empleado> empleadosEmpresa4 = new ArrayList<>();

        Empresa empresa = new Empresa(1,"ABC",empleadosEmpresa1, TipoEmpresa.PYME);
        Empresa empresa2 = new Empresa(2, "DEF",empleadosEmpresa2, TipoEmpresa.PYME);
        Empresa empresa3 = new Empresa(3, "GHI", empleadosEmpresa3, TipoEmpresa.PYME);
        Empresa empresa4 = new Empresa(4, "JKL", empleadosEmpresa4, TipoEmpresa.PYME);

        Empleado empleado1 = new Empleado(1, "12345678A", "Juan", "Pérez", "Calle Falsa 123", "555-555-555", empresa, contrato1);
        Empleado empleado2 = new Empleado(2, "23456789B", "María", "García", "Calle Falsa 456", "555-555-556", empresa2, contrato2);
        Empleado empleado3 = new Empleado(3, "34567890C", "Pedro", "López", "Calle Falsa 789", "555-555-557", empresa3, contrato3);
        Empleado empleado4 = new Empleado(4, "45678901D", "Ana", "Martínez", "Calle Falsa 012", "555-555-558", empresa4, contrato4);
        Empleado empleado5 = new Empleado(5, "56789012E", "Jorge", "Sánchez", "Calle Falsa 345", "555-555-559", empresa, contrato5);
        Empleado empleado6 = new Empleado(6, "67890123F", "Lucía", "Gómez", "Calle Falsa 678", "555-555-560", empresa2, contrato6);
        Empleado empleado7 = new Empleado(7, "78901234G", "Carlos", "Hernández", "Calle Falsa 901", "555-555-561", empresa3, contrato7);
        Empleado empleado8 = new Empleado(8, "89012345H", "Sara", "Jiménez", "Calle Falsa 234", "555-555-562", empresa4, contrato8);
        Empleado empleado9 = new Empleado(9, "90123456I", "David", "Pérez", "Calle Falsa 567", "555-555-563", empresa, contrato9);
        Empleado empleado10 = new Empleado(10, "01234567J", "Laura", "García", "Calle Falsa 890", "555-555-564", empresa2, contrato10);
        Empleado empleado11 = new Empleado(11, "12345678K", "Javier", "López", "Calle Falsa 123", "555-555-565", empresa3, contrato1);
        Empleado empleado12 = new Empleado(12, "23456789L", "Carmen", "Martínez", "Calle Falsa 456", "555-555-566", empresa4, contrato2);
        Empleado empleado13 = new Empleado(13, "34567890M", "Manuel", "Sánchez", "Calle Falsa 789", "555-555-567", empresa2, contrato3);
        Empleado empleado14 = new Empleado(14, "45678901N", "Isabel", "Gómez", "Calle Falsa 012", "555-555-568", empresa2, contrato4);
        Empleado empleado15 = new Empleado(15, "56789012O", "Miguel", "Hernández", "Calle Falsa 345", "555-555-569", empresa3, contrato5);
        Empleado empleado16 = new Empleado(16, "67890123P", "Elena", "Jiménez", "Calle Falsa 678", "555-555-570", empresa4, contrato6);
        Empleado empleado17 = new Empleado(17, "78901234Q", "Antonio", "Pérez", "Calle Falsa 901", "555-555-571", empresa, contrato7);
        Empleado empleado18 = new Empleado(18, "89012345R", "Raquel", "García", "Calle Falsa 234", "555-555-572", empresa2, contrato8);
        Empleado empleado19 = new Empleado(19, "90123456S", "Francisco", "López", "Calle Falsa 567", "555-555-573", empresa3, contrato9);
        Empleado empleado20 = new Empleado(20, "01234567T", "Cristina", "Martínez", "Calle Falsa 890", "555-555-574", empresa4, contrato10);
        Empleado empleado21 = new Empleado(21, "12345678U", "Pablo", "Sánchez", "Calle Falsa 123", "555-555-575", empresa2, contrato1);

        List<Empleado> empleados = new ArrayList<>(List.of(empleado1,empleado2,empleado3,empleado4,empleado5,empleado6,empleado7,empleado8,empleado9,empleado10,empleado11,empleado12,empleado13,empleado14,empleado15,empleado16,empleado17,empleado18,empleado19,empleado20,empleado21));

        empleadosEmpresa1.add(empleado1);
        empleadosEmpresa1.add(empleado5);
        empleadosEmpresa1.add(empleado9);
        empleadosEmpresa1.add(empleado21);
        empleadosEmpresa2.add(empleado17);

        empleadosEmpresa2.add(empleado2);
        empleadosEmpresa2.add(empleado6);
        empleadosEmpresa2.add(empleado10);
        empleadosEmpresa2.add(empleado13);
        empleadosEmpresa2.add(empleado14);
        empleadosEmpresa2.add(empleado20);
        empleadosEmpresa2.add(empleado16);

        empleadosEmpresa3.add(empleado3);
        empleadosEmpresa3.add(empleado7);
        empleadosEmpresa3.add(empleado11);
        empleadosEmpresa2.add(empleado19);
        empleadosEmpresa2.add(empleado15);

        empleadosEmpresa4.add(empleado4);
        empleadosEmpresa4.add(empleado8);
        empleadosEmpresa4.add(empleado12);
        empleadosEmpresa2.add(empleado18);

        empresa.setEmpleados(empleadosEmpresa1);
        empresa2.setEmpleados(empleadosEmpresa2);
        empresa3.setEmpleados(empleadosEmpresa3);
        empresa4.setEmpleados(empleadosEmpresa4);

        List<Empresa> empresas = new ArrayList<>(List.of(empresa,empresa2,empresa3,empresa4));

//        System.out.println(UtilidadesEmpleado.getEmpleadosPorLetraDNI(empleados));
//
//        System.out.println(UtilidadesEmpleado.getEmpleadosPorEmpresa(empleados));

        System.out.println(UltilidadesEmpresa.getEmpleadosPorTipoContrato(empresa));
        System.out.println(UltilidadesEmpresa.getEmpleadosPorTipoContrato(empresas));

    }
}
