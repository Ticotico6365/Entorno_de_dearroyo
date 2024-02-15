import enumenadores.TipoContrato;
import enumenadores.TipoEmpresa;
import modelos.Contrato;
import modelos.Empleado;
import modelos.Empresa;
import utilidades.UltilidadesEmpresa;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class pruebaV3 {
    public static void main(String[] args) {
        Empresa empresa = new Empresa(1,"1", new ArrayList<>(), TipoEmpresa.PYME);

        Contrato contrato = new Contrato(1,2000D,TipoContrato.INDEFINIDO);
        Contrato contrato2 = new Contrato(1,1000D,TipoContrato.INDEFINIDO);

        Empleado empleado1 = new Empleado(1,"12345678j","Pepe","Lopez","Calle amapola 6","665568974",empresa, contrato);
        Empleado empleado2 = new Empleado(1,"12345678k","Antonio","Martínez","Calle frederico 6","74122545558",empresa, contrato2);

        empresa.setEmpleados(new ArrayList<>(List.of(empleado1)));

        System.out.println(UltilidadesEmpresa.getEmpleadosPorContrato(empresa,TipoContrato.INDEFINIDO));

        System.out.println(UltilidadesEmpresa.getMileuristasOrdenadosPorSalario2(empresa));

        System.out.println(UltilidadesEmpresa.fondoSalarialEmpresa(empresa));
    }
}
