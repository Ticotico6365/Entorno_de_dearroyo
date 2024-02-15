package utilidades;

import enumenadores.TipoContrato;
import modelos.Contrato;
import modelos.Empleado;
import modelos.Empresa;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class UtidadesContrato {
    //a
    public static Map<TipoContrato, Double> getSalarioMedioTipoContrato(List<Contrato> contratos){
        // creamos mapa final
        Map<TipoContrato, Double> mediaContartos = new HashMap<>();
        // mapa de con todos los salarios po contrato
        Map<TipoContrato, List<Double>> listaSalarioPorContrato = new HashMap<>();
        //rrellenado
        for (Contrato i : contratos){
            listaSalarioPorContrato.put(i.getTipoContrato(), new ArrayList<>());
        }
        //rellenado
        for (Contrato i : contratos){
            listaSalarioPorContrato.get(i.getTipoContrato()).add(i.getSalarioBase());
        }
        //completamos el mapa final
        for(TipoContrato i : listaSalarioPorContrato.keySet()){
            Double total = 0D;
            for(Double j : listaSalarioPorContrato.get(i)){
                total += j;
            }
           Double media = total/listaSalarioPorContrato.get(i).size();
           mediaContartos.put(i,media);

        }
        return mediaContartos;
    }
    //b
    public static Map<TipoContrato, Integer> getNumContratosPorTipo(List<Contrato> contratos){
        Map<TipoContrato, List<Double>> listaSalarioPorContrato = new HashMap<>();
        for (Contrato i : contratos){
            listaSalarioPorContrato.put(i.getTipoContrato(), new ArrayList<>());
        }
        for (Contrato i : contratos){
            listaSalarioPorContrato.get(i.getTipoContrato()).add(i.getSalarioBase());
        }
        Map<TipoContrato, Integer> mapaFinal = new HashMap<>();
        for(TipoContrato i : listaSalarioPorContrato.keySet()){
            mapaFinal.put(i,listaSalarioPorContrato.get(i).size());
        }
        return mapaFinal;
    }

    //c
    public static Map<TipoContrato, List<Contrato>> getListContratosPorTipo(List<Contrato> contratos) {
        Map<TipoContrato, List<Contrato>> mapaFinal = new HashMap<>();
        for (Contrato i : contratos) {
            mapaFinal.put(i.getTipoContrato(), new ArrayList<>());
        }
        for (Contrato i : contratos) {
            mapaFinal.get(i.getTipoContrato()).add(i);
        }
        return mapaFinal;
    }

    //V5
    public Empleado contratarTrabajador(Empresa e, String dni, String nombre, String apellidos, String direccion, String telefono, TipoContrato tipo, Double salario){
        Empleado empleado = new Empleado();
        Contrato contrato = new Contrato(Generador.crearContrato());

        empleado.setNombre(nombre);
        empleado.setApellidos(apellidos);
        empleado.setDireccion(direccion);
        empleado.setNumTelefono(telefono);
        contrato.setTipoContrato(tipo);
        contrato.setSalarioBase(salario);
        empleado.setDni(dni);
        empleado.setEmpresa(e);

        return empleado;

    }


}
