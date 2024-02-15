package utilidades;

import modelos.Empleado;
import modelos.Empresa;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class UtilidadesEmpleado {
    //a
    public static Map<String, List<Empleado>> getEmpleadosPorLetraDNI(List<Empleado> empleados) {
        Map<String, List<Empleado>> empleadoPorLetraDNI = new HashMap<>();

        for (Empleado i : empleados) {
            empleadoPorLetraDNI.put(String.valueOf(i.getDni().charAt(i.getDni().length() - 1)), new ArrayList<>());
        }
        for (Empleado i : empleados) {
            empleadoPorLetraDNI.get(String.valueOf(i.getDni().charAt(i.getDni().length() - 1))).add(i);
        }
        return empleadoPorLetraDNI;
    }
    //b
    public static Map<Empresa, List<Empleado>> getEmpleadosPorEmpresa(List<Empleado> empleados) {
        Map<Empresa, List<Empleado>> empleadoPorEmpresa = new HashMap<>();
        for (Empleado i : empleados) {
            empleadoPorEmpresa.put(i.getEmpresa(), new ArrayList<>());
        }
        for (Empleado i : empleados) {
            empleadoPorEmpresa.get(i.getEmpresa()).add(i);
        }
        return empleadoPorEmpresa;
    }

}
