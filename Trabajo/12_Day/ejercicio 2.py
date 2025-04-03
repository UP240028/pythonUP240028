#ejercicio 1
print("")
print("Ejercicio 1")

import random

def list_of_hexa_colors():
    n = random.randint(0, 10)
    s = "0123456789abcdef"
    lst = []
    for i in range(n):
        res = '#'
        for j in range(6):
            res += random.choice(s)
        lst.append(res)
    return lst
print(list_of_hexa_colors())

#ejercicio 2
print("")
print("Ejercicio 2")

def list_of_rgb_colors():
    n = random.randint(0, 10)
    lst = []
    for i in range(n):
        r = random.randint(0, 256)
        b = random.randint(0, 256)
        g = random.randint(0, 256)
        lst.append(f"rgb({r},{b},{g})")
    return lst
print(list_of_rgb_colors())

#ejercicio 3

print("")
print("Ejercicio 3")

def generate_colors(type, n):
    if type == 'hexa':
        s = "0123456789abcdef"
        lst = []
        for i in range(n):
            res = '#'
            for j in range(6):
                res += random.choice(s)
            lst.append(res)
        print(lst)
    elif type == 'rgb':
        lst = []
        for i in range(n):
            r = random.randint(0, 256)
            b = random.randint(0, 256)
            g = random.randint(0, 256)
            lst.append(f"rgb({r},{b},{g})")
        print(lst)
    else:
        print("Enter type correctly")


print(generate_colors('hexa', 5))           
print(generate_colors('rgb', 3))