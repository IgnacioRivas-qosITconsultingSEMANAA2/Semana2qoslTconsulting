# Ejercicio 1: Creación de una Clase Básica
class Libro:
    def __init__(self, titulo, autor, año_publicacion, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.__disponible = disponible  # Atributo privado
    
    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")
    
    def devolver(self):
        self.__disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")
    
    def mostrar_info(self):
        estado = "Disponible" if self.__disponible else "No disponible"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.año_publicacion}, Estado: {estado}")

# Ejercicio 2: Herencia
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas
    
    def info(self):
        return super().info() + f", Puertas: {self.puertas}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada
    
    def info(self):
        return super().info() + f", Cilindrada: {self.cilindrada} cc"

# Ejercicio 3: Encapsulamiento
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo      # Atributo privado
    
    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f"Se han depositado {cantidad}. Saldo actual: {self.__saldo}")
    
    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se han retirado {cantidad}. Saldo actual: {self.__saldo}")
        else:
            print("Saldo insuficiente.")
    
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")

# Ejercicio 4: Polimorfismo
class FiguraGeometrica:
    def calcular_area(self):
        pass

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2

# Ejercicio 5: Proyecto Final
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
    
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False
    
    def devolver(self):
        self.disponible = True

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def prestar_libro(self, titulo, usuario):
        for libro in self.libros:
            if libro.titulo == titulo and libro.prestar():
                print(f"{usuario.nombre} ha tomado prestado '{titulo}'")
                return
        print(f"El libro '{titulo}' no está disponible.")
    
    def devolver_libro(self, titulo, usuario):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.devolver()
                print(f"{usuario.nombre} ha devuelto '{titulo}'")
                return
        print(f"El libro '{titulo}' no pertenece a la biblioteca.")
