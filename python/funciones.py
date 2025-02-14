def saludo():
    print("Hola, soy una función")

def suma(a, b):
    return a + b


resultado = suma(5, 3)
print("La suma es: ", + resultado)


num = int (input("Introduce un número: "))

def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    

print(es_par(num))
  