#ejercicio 1
print("")
print("Ejercicio 1")

import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst
print(shuffle_list([1,2,3,4,5,6]))

#ejercicio 2
print("")
print("Ejercicio 2")

def seven_random():
    s = set()
    lst = []
    while True:
        if len(s) == 7:
            lst = s
            return lst
        n = random.randint(0, 10)
        s.add(n)
print(seven_random())