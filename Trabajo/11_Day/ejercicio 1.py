#ejercicio 1
print("")
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

#ejercicio 2
print("")
def AreaCirculo():
    pi = 3.1416
    radio = 5
    area = pi * radio * radio
    print(area)
print(AreaCirculo())

#ejercicio 3
print("")
def add_all_nums (*args):
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return f"Error: '{arg}' no es un número. Por favor, proporciona solo valores numéricos."
        total += arg
    return total

#ejercicio 4
print("")
def convert_celsius_to_fahrenheit():
    celcius = float(input("Ingresa la temperatura en grados Celcius: "))
    Farenheit = (celcius * 1.8) + 32
    print(Farenheit)
print(convert_celsius_to_fahrenheit())

#ejercicio 5
print("")
Mes = str(input("Ingrese el mes: "))
def ChecarTemporada():
    if Mes in ["Septiembre", "Octubre", "Noviembre"]:
        print("Otoño")
    elif Mes in ["Diciembre", "Enero", "Febrero"]:
        print("Invierno")
    elif Mes in ["Marzo", "Abril", "Mayo"]:
        print("Primavera")
    elif Mes in ["Junio", "Julio", "Agosto"]:
        print("Verano")
    else:
        print("No existe")

#ejercicio 6
print("")
def calculate_slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

#ejercicio 7
print("") 
def solve_quadratic_eqn(a, b, c):
    sol1 = (-(b) + ((b)**2 - 4*a*c)**0.5)/(2*a)
    sol2 = (-(b) - ((b)**2 - 4*a*c)**0.5)/(2*a)
    print(f"Sol1 : {sol1}")
    print(f"Sol2 : {sol2}")

#ejercicio 8
print("")
def print_list(lst):
    for i in lst:
        print(i)
print_list([1, 2, 6, 8, 3])

#ejercicio 9
print("")
def reverse_list(lst):
    new_lst = []
    for i in range(-1, -(len(lst))-1, -1):
        new_lst.append(lst[i])
    return new_lst
print(reverse_list([1, 2, 3, 4]))

#ejercicio 10
print("")
def capitalize_list_items(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item.capitalize())
    return new_lst
print(capitalize_list_items(['hello', 'world']))

#ejercicio 11
print("")
def add_item(lst, item):
    lst.append(item)
    return lst
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

#ejercicio 12
print("")
def remove_item(lst, item):
    lst.remove(item)
    return lst


numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

#ejercicio 13
print("")
def sum_of_numbers(r):
    sum = 0
    for i in range(r+1):
        sum += i
    return sum


print(sum_of_numbers(5))

#ejercicio 14
def sum_of_odds(r):
    sum = 0
    for i in range(r+1):
        if i % 2 != 0:
            sum += i
    return sum

#ejercicio 15
print("")
def sum_of_numbers(r):
    sum = 0
    for i in range(r+1):
        if i % 2 == 0:
            sum += i
    return sum

print("revisado")