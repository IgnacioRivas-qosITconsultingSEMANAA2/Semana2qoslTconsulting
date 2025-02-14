'''
print("Comparación de números")


if True:
    print("Hola")
    print("Mundo")

    a = 5
    
    if a == 2:
        print("a es igual a 2 ")
    if a == 5:
        print("a es igual a 5")

n = int(input("Introduce un número: "))

if n % 2 == 0:
    print("n es par")
else:
    print("n es impar")

nota = float(input("Introduce una nota: "))

if nota < 5:
    print("Suspendido")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")

    print("Fin del programa")
'''
print("Bucles")

c = 0

while c <= 5: 
    c+= 1
    print("c vale", c)


for i in range(1,11):
    print("Tabla del", i)
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")


numero = int(input("Introduce un numero y da la tabla de ese numero: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero*i}")
    