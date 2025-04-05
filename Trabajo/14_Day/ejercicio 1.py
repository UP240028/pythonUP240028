# 1. Diferencia entre map, filter y reduce
# - map() aplica una función a cada elemento de un iterable y devuelve un nuevo iterable con los resultados.
# - filter() filtra los elementos de un iterable según una función de prueba, devolviendo solo los elementos que pasan la prueba.
# - reduce() acumula los resultados de aplicar una función a los elementos de un iterable, devolviendo un solo valor.

# 2. Diferencia entre higher order function, closure y decorator
# - Higher Order Function: Una función que puede aceptar otra función como argumento o devolver una función.
# - Closure: Una función interna que recuerda el entorno en el que fue creada, incluso después de que la función externa haya terminado.
# - Decorator: Una función que modifica el comportamiento de otra función sin modificarla directamente.

#ejercicio 3
def call_func(func):
    func()

def hello_world():
    print("¡Hola, Mundo!")

call_func(hello_world)

# ejercicio 4
print("")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

#ejercicio 5
print("")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)

#ejercicio 6 
print("")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)
