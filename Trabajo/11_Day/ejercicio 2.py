#ejercicio 1
print("")
def evens_and_odds(r):
    ecount = 0
    ocount = 0
    for i in range(r+1):
        if i % 2 == 0:
            ecount += 1
        else:
            ocount += 1
    print(f"The number of odds are {ocount}.")
    print(f"The number of evenss are {ecount}.")
evens_and_odds(100)

#ejercicio 2
print("")
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(5))

#ejercicio 3
print("")
def is_empty(a):
    if len(a):
        print("Not Empty")
    else:
        print("Empty")

#Escriba diferentes funciones que acepten listas
from statistics import mean, median, mode, stdev, variance

def calcular_media(lista):
    return mean(lista)

def calcular_mediana(lista):
    return median(lista)

def calcular_moda(lista):
    return mode(lista)

def calcular_rango(lista):
    return max(lista) - min(lista)

def calcular_varianza(lista):
    return variance(lista)

def calcular_desviacion_estandar(lista):
    return stdev(lista)
datos = [1, 2, 2, 3, 4, 5, 6, 7]

print("Media:", calcular_media(datos))
print("Mediana:", calcular_mediana(datos))
print("Moda:", calcular_moda(datos))
print("Rango:", calcular_rango(datos))
print("Varianza:", calcular_varianza(datos))
print("Desviación estándar:", calcular_desviacion_estandar(datos))


print("revisado")