package utilidades;

import enumenadores.TipoContrato;
import enumenadores.TipoEmpresa;
import modelos.Empleado;
import modelos.Empresa;

import java.util.*;
import java.util.stream.Collectors;

public class UltilidadesEmpresa {
    //a
    public static List<Empleado> getEmpleadosPorContrato(Empresa empresa, TipoContrato tipoContrato){
        List<Empleado> list = new ArrayList<>();
        for(Empleado emp : empresa.getEmpleados()){
            if (emp.getContrato().getTipoContrato().equals(tipoContrato)){
                list.add(emp);
            }
        }
        return list;
    }

    public static List<Empleado> getEmpleadosPorContratoStream (Empresa empresa, TipoContrato tipoContrato){
        return empresa.getEmpleados()
                .stream()
                .filter(e->e.getContrato().getTipoContrato().equals(tipoContrato)).collect(Collectors.toList());
    }

    //b
    public static List<Empleado> getMileuristasOrdenadosPorSalario(Empresa empresa){
        Map<Empleado, Double> empleadoSalario = new HashMap<>();
        for (Empleado emp : empresa.getEmpleados()){
            if (emp.getContrato().getSalarioBase() >= 1000){
                empleadoSalario.put(emp, emp.getContrato().getSalarioBase());
            }
        }
        List<Map.Entry<Empleado, Double>> list = new ArrayList<>(empleadoSalario.entrySet());
        list.sort(Map.Entry.comparingByValue());

        Map<Empleado, Double> empleadoSalarioOrdenado = new LinkedHashMap<>();
        for (Map.Entry<Empleado, Double> entry : list) {
            empleadoSalarioOrdenado.put(entry.getKey(), entry.getValue());
        }

        return new ArrayList<>(empleadoSalarioOrdenado.keySet());
    }

    public static List<Empleado> getMileuristasOrdenadosPorSalario2(Empresa empresa){
        List<Empleado> empleados = new ArrayList<>();
        for (Empleado e : empresa.getEmpleados()){
            if (e.getContrato().getSalarioBase() >= 1000){
                empleados.add(e);
            }
        }

        //orden natural
    empleados.sort(Comparator.comparing(e->e.getContrato().getSalarioBase()));
        //dar la vuelta
    empleados.reversed();


    return empleados;
    }

    public static List<Empleado> getMileuristasOrdenadosPorSalario2Stream(Empresa empresa){
        return empresa.getEmpleados()
                .stream()
                .filter(e->e.getContrato().getSalarioBase() >= 1000)
                .sorted(Comparator.comparingDouble(e->e.getContrato().getSalarioBase()))
                .collect(Collectors.toList())
                .reversed();
    }

    //c
    public static double fondoSalarialEmpresa(Empresa empresa){
        Double total = 0D;
        for (Empleado emp : empresa.getEmpleados()){
           total += emp.getContrato().getSalarioBase();
        }
        return total;
    }

    //d
    public static Empleado getMejorPagado(List<Empresa> empresas){

        //juntar todos los empleados de todas las empresas
        List<Empleado> empleados = new ArrayList<>();

        for(Empresa e : empresas){
            empleados.addAll(e.getEmpleados());
        }
        //ordenarlo de menor a mayor
        empleados.sort(Comparator.comparing(e->e.getContrato().getSalarioBase()));
        //tomar el último elemento

        return empleados.get(empleados.size()-1);
    }

    public static Map<TipoContrato, List<Empleado>> getEmpleadosPorTipoContrato(Empresa empresas){
        Map<TipoContrato, List<Empleado>> mapaFinal = new HashMap<>();

        for(Empleado i : empresas.getEmpleados()){
            mapaFinal.put(i.getContrato().getTipoContrato(),new ArrayList<>());
        }
        for (Empleado i : empresas.getEmpleados()){
            mapaFinal.get(i.getContrato().getTipoContrato()).add(i);
        }
        return mapaFinal;
    }

    public static Map<Empresa, Map<TipoContrato, List<Empleado>>> getEmpleadosPorTipoContrato(List<Empresa> empresas){
        Map<Empresa, Map<TipoContrato, List<Empleado>>> mapaFinal = new HashMap<>();

        for(Empresa i : empresas){
            mapaFinal.put(i, getEmpleadosPorTipoContrato(i));
        }
        return mapaFinal;
    }

    public static List<Empleado> getEmpleadosPymePracticas(List<Empresa> empresas){
        List<Empleado> empresaList = new ArrayList<>();
        for (Empresa i : empresas){
            for (Empleado j : i.getEmpleados()){
                if (j.getEmpresa().getTipoEmpresa().equals(TipoEmpresa.PYME) && j.getContrato().getTipoContrato().equals(TipoContrato.PRACTICAS)){
                    empresaList.add(j);
                }
            }
        }
        return empresaList;
    }

    public static Map<Empresa, Empleado> getLosMejorPagadosPorEmpresa(List<Empresa> empresas) {
        Map<Empresa, Empleado> mapaFinal = new HashMap<>();

        for (Empresa i : empresas) {
            mapaFinal.put(i, new Empleado());
            for (Empleado j : i.getEmpleados()) {
                if (mapaFinal.get(i).getContrato().getSalarioBase() < j.getContrato().getSalarioBase()) {
                    mapaFinal.put(i, j);
                }
            }
        }
        return mapaFinal;
    }

    public Map<TipoEmpresa, Integer> getNumEmpleadosPorTipoEmpresa(List<Empresa> empresas){
        Map<TipoEmpresa, Integer> mapaFinal = new HashMap<>();

        for (Empresa i : empresas){
            mapaFinal.put(i.getTipoEmpresa(), mapaFinal.get(i.getTipoEmpresa()) + i.getEmpleados().size());
        }
        return mapaFinal;
    }


}
