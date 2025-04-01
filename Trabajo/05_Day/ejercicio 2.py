#ejercicio 1
print("")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

min_age = min(ages)
max_age = max(ages)

#Paso 2
print("Lista ordenada:", ages)
print("Edad mínima:", min_age)
print("Edad máxima:", max_age)

ages.append(min_age)
ages.append(max_age)

print("Lista después de agregar la edad mínima y máxima:", ages)

n = len(ages)
if n % 2 == 1:
    median = ages[n // 2]
else:
    median = (ages[n // 2 - 1] + ages[n // 2]) / 2

#paso 3
print("Edad mediana:", median)

#paso 4
average_age = sum(ages) / len(ages)
print("Edad promedio:", average_age)

#paso 5
age_range = max_age - min_age
print("Rango de edades:", age_range)

#Paso 6
min_vs_avg = abs(min_age - average_age)
max_vs_avg = abs(max_age - average_age)

print(f"Valor absoluto de (mín - promedio): {min_vs_avg}")
print(f"Valor absoluto de (máx - promedio): {max_vs_avg}")

#ejercicio 2
print("")
# Lista de países
countries = ['China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']

# Paso 1:
n = len(countries)
if n % 2 == 1:
    paises_medio = countries[n // 2] 
    print("País del medio:", paises_medio)
else:
    paises_medio = countries[n // 2 - 1:n // 2 + 1] 
    print("Países del medio:", paises_medio)

# Paso 2:
half_index = (n // 2) + (n % 2)  
first_half = countries[:half_index]
second_half = countries[half_index:]

print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)

# Paso 3:
scandinavian_countries = second_half
first_three_countries = first_half[:3]

print("Primeros tres países:", first_three_countries)
print("Países escandinavos:", scandinavian_countries)

print("Revisado")