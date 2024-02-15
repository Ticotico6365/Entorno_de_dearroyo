package modelos;

import enumenadores.TipoEmpresa;

import java.util.List;

public class Empresa {
    private Integer identificador;
    private String codigoEmpresa;
    private List<Empleado> empleados;
    private TipoEmpresa tipoEmpresa;

    //getter-setter
    public Integer getIdentificador() {
        return identificador;
    }

    public void setIdentificador(Integer identificador) {
        this.identificador = identificador;
    }

    public String getCodigoEmpresa() {
        return codigoEmpresa;
    }

    public void setCodigoEmpresa(String codigoEmpresa) {
        this.codigoEmpresa = codigoEmpresa;
    }

    public List<Empleado> getEmpleados() {
        return empleados;
    }

    public void setEmpleados(List<Empleado> empleados) {
        this.empleados = empleados;
    }

    public TipoEmpresa getTipoEmpresa() {
        return tipoEmpresa;
    }

    public void setTipoEmpresa(TipoEmpresa tipoEmpresa) {
        this.tipoEmpresa = tipoEmpresa;
    }

    //constructores
        //vacio
    public Empresa() {
    }
        //completo
    public Empresa(Integer identificador, String codigoEmpresa, List<Empleado> empleados, TipoEmpresa tipoEmpresa) {
        this.identificador = identificador;
        this.codigoEmpresa = codigoEmpresa;
        this.empleados = empleados;
        this.tipoEmpresa = tipoEmpresa;
    }
        //copia
    public Empresa(Empresa empresa){
        this.identificador = empresa.getIdentificador();
        this.codigoEmpresa = empresa.getCodigoEmpresa();
        this.empleados = empresa.getEmpleados();
        this.tipoEmpresa = empresa.getTipoEmpresa();
    }

    //toString

    @Override
    public String toString() {
        return "Empresa{" +
                "identificador=" + identificador +
                ", codigoEmpresa='" + codigoEmpresa + '\'' +
                //", empleados=" + empleados +
                ", tipoEmpresa=" + tipoEmpresa +
                '}';
    }
}
