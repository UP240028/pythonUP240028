#ejercicio 1
print("Ejercicio 1:")#buicel con for
numbers=(0,1,2,3,4,5,6,7,8,9,10)
for number in numbers:
    print(number)

#ejercicio 2
print("")
print("Ejercicio 2:")#bucle con while
i = 0
while i < 11 : 
    print(i)
    i += 1

#ejercico 3
print("")
print("Ejercicio 3")
for i in range(8):
    print("#"*i)


#ejercicio 4
print("")
print("Ejercicio 4:")
for i in range(8):
    print("# "*8)
print("")#metodo 2 y oficial
for i in range(8):
    for j in range(8):
          print("#", end=" ")
    print("")

#ejercicio 5
print("")
print("Ejercicio 5:")
i=0
while i < 11:
    print(i," x ",i,"= ",i*i)
    i += 1

#ejercicio 6
print("")
print("Ejercio 6:")
print("")
item=['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item1 in item:
    print(item1)

#ejercicio 7
print("")
print("Ejercicio 7:")
for i in range(100):
    if i % 2 == 0:
        print(i)

#ejercicio 8
print("")
print("Ejercicio 7:")
for i in range(100):
    if i % 2 !=0:
        print(i)