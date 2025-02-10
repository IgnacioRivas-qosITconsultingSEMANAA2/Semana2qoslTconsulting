
package persona;

import java.util.ArrayList;
import java.util.List;

public class Curso {
    private String nombreCurso;
    private Profesor profesor;
    private List<Estudiante> estudiantes;

    public Curso(String nombreCurso, Profesor profesor) {
        this.nombreCurso = nombreCurso;
        this.profesor = profesor;
        this.estudiantes = new ArrayList<>();
    }

    public void matricularEstudiante(Estudiante estudiante) {
        estudiantes.add(estudiante);
        System.out.println(estudiante.getNombre() + " ha sido matriculado en el curso " + nombreCurso);
    }

    public void mostrarEstudiantes() {
        System.out.println("Estudiantes del curso " + nombreCurso + ":");
        for (Estudiante estudiante : estudiantes) {
            estudiante.mostrarInformacion();
        }
    }

    public void mostrarProfesor() {
        System.out.println("Profesor del curso " + nombreCurso + ":");
        profesor.mostrarInformacion();
    }
}
