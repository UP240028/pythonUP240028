#ejercicio 1
print("")
print("Ejercicio 1")

import random


def random_user_id():
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    res = ''
    for i in range(6):
        res += random.choice(s)
    return res
print(random_user_id())

#ejercicio 2
print("")
print("Ejercicio 2")

def user_id_gen_by_user():
    n = int(input("Enter n : "))
    t = int(input("Enter t : "))
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in range(t):
        res = ''
        for j in range(n):
            res += random.choice(s)
        print(res)
print(user_id_gen_by_user())

#ejercicio 3
print("")
print("Ejercicio 3")

def rgb_color_gen():
    r = random.randint(0, 256)
    b = random.randint(0, 256)
    g = random.randint(0, 256)
    return f"rgb({r},{b},{g})"
print(rgb_color_gen())