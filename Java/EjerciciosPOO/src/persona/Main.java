package persona;



import persona.Persona;

public class Main {
 public static void main(String[] args) {
    //ejercicio 1
       /* Persona persona1 = new Persona("Luis", 30);
        System.out.println("Nombre: " + persona1.getNombre() + ", Edad: " + persona1.getEdad());
        */ 
        //ejercicio 2
        /*
        Persona persona1 = new Persona("Luis", 30);
        Persona persona2 = new Persona("Luis", 30);
        Persona persona3 = new Persona("Ana", 25);

        System.out.println("Nombre: " + persona1.getNombre() + ", Edad: " + persona1.getEdad());
        System.out.println("persona1 es igual a persona2: " + persona1.equals(persona2));
        System.out.println("persona1 es igual a persona3: " + persona1.equals(persona3));
    */
   /* 
    Persona persona1 = new Persona("Luis", 30);
    Persona persona2 = new Persona("Luis", 30);
    Persona persona3 = new Persona("Ana", 25);

    persona1.mostrarInformacion();
    System.out.println("persona1 es igual a persona2: " + persona1.equals(persona2));
    System.out.println("persona1 es igual a persona3: " + persona1.equals(persona3));

    Estudiante estudiante1 = new Estudiante("Carlos", 20, "Ingeniería");
    estudiante1.mostrarInformacion();
    */
    /* 
    Estudiante estudiante = new Estudiante("Carlos", 20, "Ingeniería");
    System.out.println(estudiante.toString());
    estudiante.estudiar();
    */
    /*
    Profesor profesor = new Profesor("Dr. García", 45, "Matemáticas");
        profesor.mostrarInformacion();
        profesor.trabajar();
        */
        /*
        Persona[] personas = new Persona[3];
        personas[0] = new Persona("Pedro", 40);
        personas[1] = new Estudiante("Ana", 22, "Medicina");
        personas[2] = new Profesor("Dr. López", 50, "Física");

        for (Persona persona : personas) {
            persona.mostrarInformacion();
            if (persona instanceof Trabajador) {
                ((Trabajador) persona).trabajar();
            }
        }
            */
        /*
        Direccion direccion = new Direccion("Calle Pino Alto", "Sanlucar De Barrameda", "11540");
        Persona persona = new Persona("Nashee", 30, direccion);
        persona.mostrarInformacion();
        persona.mostrarDireccion();
        */
        
/*
        Persona persona1 = new Persona("Carlos", 25);
        Persona persona2 = new Persona("Ana", 30);
        
        int resultado = persona1.comparar(persona2);
        if (resultado == 0) {
            System.out.println("Las dos personas tienen la misma edad.");
        } else if (resultado > 0) {
            System.out.println(persona1.getNombre() + " es mayor que " + persona2.getNombre());
        } else {
            System.out.println(persona1.getNombre() + " es menor que " + persona2.getNombre());
        }
    */

        // Crear profesores
        Profesor profesor1 = new Profesor("Dr. García", 45, "Matemáticas");
        Profesor profesor2 = new Profesor("Dra. López", 50, "Física");

        // Crear estudiantes
        Estudiante estudiante1 = new Estudiante("Juan", 20, "Ingeniería");
        Estudiante estudiante2 = new Estudiante("Ana", 22, "Medicina");
        Estudiante estudiante3 = new Estudiante("Carlos", 21, "Derecho");

        // Crear cursos
        Curso curso1 = new Curso("Álgebra Lineal", profesor1);
        Curso curso2 = new Curso("Mecánica Clásica", profesor2);

        // Matricular estudiantes en los cursos
}

}

