#ejercicio 1 y 2
print("")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#ejercicio 3
print("")
def elementos_unicos(lista):
    return len(lista) == len(set(lista))
datos = [1, 2, 3, 4, 5]
print("¿Todos los elementos son únicos?", elementos_unicos(datos))
datos_repetidos = [1, 2, 3, 4, 2]
print("¿Todos los elementos son únicos?", elementos_unicos(datos_repetidos))

#ejercicio 4    
print("")
def mismos_tipos(lista):
    if not lista:
        return True
    tipo_referencia = type(lista[0])
    return all(type(elemento) == tipo_referencia for elemento in lista)
datos1 = [1, 2, 3, 4]
print("¿Todos los elementos son del mismo tipo?", mismos_tipos(datos1))
datos2 = [1, "texto", 3.5]
print("¿Todos los elementos son del mismo tipo?", mismos_tipos(datos2))

#ejercicio 5
print("")
import keyword
def es_variable_valida(nombre):
    if not nombre.isidentifier():
        return False
    if nombre in keyword.kwlist:
        return False
    return True
variable1 = "mi_variable"
print(f"¿'{variable1}' es una variable válida?", es_variable_valida(variable1))
variable2 = "1variable"
print(f"¿'{variable2}' es una variable válida?", es_variable_valida(variable2))
variable3 = "for"
print(f"¿'{variable3}' es una variable válida?", es_variable_valida(variable3))


print("revisado")