package modelos;

import enumenadores.TipoContrato;

public class Contrato {
    private Integer identificador;
    private Double salarioBase;
    private TipoContrato tipoContrato;

    //getter-setter

    public Integer getIdentificador() {
        return identificador;
    }

    public void setIdentificador(Integer identificador) {
        this.identificador = identificador;
    }

    public Double getSalarioBase() {
        return salarioBase;
    }

    public void setSalarioBase(Double salarioBase) {
        this.salarioBase = salarioBase;
    }

    public TipoContrato getTipoContrato() {
        return tipoContrato;
    }

    public void setTipoContrato(TipoContrato tipoContrato) {
        this.tipoContrato = tipoContrato;
    }

    //construciones
        //vacio
    public Contrato() {
    }
        //completo
    public Contrato(Integer identificador, Double salarioBase, TipoContrato tipoContrato) {
        this.identificador = identificador;
        this.salarioBase = salarioBase;
        this.tipoContrato = tipoContrato;
    }
        //copia
    public Contrato(Contrato contrato){
        this.identificador = contrato.getIdentificador();
        this.salarioBase = contrato.getSalarioBase();
        this.tipoContrato = contrato.getTipoContrato();
    }

    //teString

    @Override
    public String toString() {
        return "Contrato{" +
                "identificador=" + identificador +
                ", salarioBase=" + salarioBase +
                ", tipoContrato=" + tipoContrato +
                '}';
    }
}
