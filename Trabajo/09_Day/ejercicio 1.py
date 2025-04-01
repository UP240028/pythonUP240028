#ejercicio 1
Edad = int(input("Ingrese su edad: "))
if Edad < 18:
    print("No tienes edad suficiente para aprender a conducir")
else:
    print("Tienes la edad suficiente para aprender a conducir")

#ejercicio 2
TuEdad = int(input("Ingresa tu edad: "))
MiEdad= int(input("Ingresa tu edad: "))
if MiEdad == TuEdad: 
    print("Tenemos la misma edad")
elif MiEdad > TuEdad:
    Dif = MiEdad - TuEdad
    if Dif:
        print("Tienes", Dif, "años más que yo")
else:
    print("El es", TuEdad - MiEdad, "años grande que tu")
#ejercicio 3
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
if a < b:
    print("a es menor que b")
elif a > b:
    print("a es mayor que b")
else:
    print("a es igual que b")

print("Revisado")