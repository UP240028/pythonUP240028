# 1. SyntaxError
# Error: olvidamos poner los paréntesis en print
# print 'Hello World'  # Esto dará SyntaxError en Python 3
print('Hello World')  # Solución: usar paréntesis

# 2. NameError
# Error: Usar una variable que no está definida
# print(age)  # Esto dará NameError
age = 25  # Definir la variable
print(age)  # Ahora debería imprimir 25

# 3. IndexError
# Error: Acceder a un índice fuera del rango de la lista
numbers = [1, 2, 3, 4, 5]
# print(numbers[5])  # Esto dará IndexError porque los índices van de 0 a 4
print(numbers[4])  # Solución: acceder a un índice válido

# 4. ModuleNotFoundError
# Error: Intentamos importar un módulo que no existe
# import maths  # Esto dará ModuleNotFoundError
import math  # Solución: importamos el módulo correcto

# 5. AttributeError
# Error: Intentar acceder a un atributo que no existe
# print(math.PI)  # Esto dará AttributeError, 'math' no tiene un atributo PI
print(math.pi)  # Solución: usar el nombre correcto del atributo 'pi'

# 6. KeyError
# Error: Intentar acceder a una clave que no existe en un diccionario
user = {'name': 'Asab', 'age': 25, 'country': 'Finland'}
# print(user['county'])  # Esto dará KeyError porque la clave es 'country' no 'county'
print(user['country'])  # Solución: usar la clave correcta 'country'

# 7. TypeError
# Error: Intentar operar con tipos incompatibles
# print(4 + '3')  # Esto dará TypeError, no podemos sumar un int y un string
print(4 + int('3'))  # Solución: convertir el string a un número entero (7)
print(4 + float('3'))  # Otra solución: convertir el string a un número flotante (7.0)

# 8. ImportError
# Error: Intentar importar una función que no existe en un módulo
# from math import power  # Esto dará ImportError porque no existe 'power' en 'math'
from math import pow  # Solución: usar el nombre correcto 'pow'
print(pow(2, 3))  # Esto dará 8.0

# 9. ValueError
# Error: Intentar convertir un string con caracteres no numéricos a un número
# print(int('12a'))  # Esto dará ValueError porque '12a' no se puede convertir a entero
print(int('12'))  # Solución: usar una cadena de texto que represente un número válido (12)

# 10. ZeroDivisionError
# Error: Intentar dividir por cero
# print(1/0)  # Esto dará ZeroDivisionError
print(1/2)  # Solución: evitar dividir entre cero
