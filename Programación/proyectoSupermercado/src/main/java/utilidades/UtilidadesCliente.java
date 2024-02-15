package utilidades;

import modelos.Cliente;

public class UtilidadesCliente {

    public static boolean esDniValido(Cliente cliente){

        String dni = cliente.getDni();
        if (dni == null){
            return false;
        }

        //tamaño
        boolean tamanyoValido = dni.length() == 9;

        //parte numérica
        String parteNumerica  = dni.substring(0, 8);
        boolean sonNumero  = parteNumerica.matches("//d+");

        //parte letra
        String letra = dni.substring(8);
        boolean esLetra = letra.matches("[A-Za-z]");

        return tamanyoValido && sonNumero && esLetra;
    }

}
