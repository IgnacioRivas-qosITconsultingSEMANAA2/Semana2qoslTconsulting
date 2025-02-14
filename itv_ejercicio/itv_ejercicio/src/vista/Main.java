package vista;

import excepciones.CamposVacioException;
import excepciones.DniException;
import excepciones.MatriculaException;
import modelo.Vehiculo;

public class Main {

    public static void main(String[] args) throws CamposVacioException {

        String nombre = "Nacho ";
        String apellidos = "Rivas Cardenas";
        String dni = "49340145Q";
        String matricula = "1224ABC";
        String identificador = "";
        Vehiculo vehiculo = null;
        try {
            vehiculo = new Vehiculo(matricula, nombre, apellidos, dni);
            System.out.println(vehiculo);
        } catch (DniException | MatriculaException e) {
            // TODO Auto-generated catch block
            System.out.println(e.getMessage());
        }
    }

}
