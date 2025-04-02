#ejercicio 1
print("Ejercicio 1:")
total_sum = 0
for i in range(101):
    total_sum += i
print("La suma de todos los números es", total_sum)

#ejercicio 2
print("")
print("Ejercicio 2:")
even_sum = 0
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("La suma de todos los números pares es:", even_sum)
print("Y la suma de todos los números impares es:", odd_sum)
