#ejercicio 1
it_companies ={'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(it_companies)
print(len(it_companies))

#ejercicio 2
print("")
it_companies.add("Twitter")
print(it_companies)

#ejercicio 3
print("")
it_companies.update(["Youtube","Tik tok"])
print(it_companies)

#ejrcicio 4
print("")
it_companies.remove("Microsoft")
print(it_companies)

#ejercicio 5
print("")
print("Diferencia entre remove y discard")
print("La diferencia es de que el discard sirve para descargar un elemento por una vez y el remove lo elimina ")

#NIVEL 2
#ejercicio 1
print("")
print("Join the A and B")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.isdisjoint(B))


#ejercicio 2
print("")
print("Interseccion entre a y b")
A.intersection(B)
print(A.intersection(B))

#ejercicio 3
print("")
print("Subet")
A.issubset(B)
print(A.issubset(B))

#ejercio 4
print("")
A = {1, 2, 3, 4}
B = {5, 6, 7, 8}
C = A.union(B)
print(C)
print("")

#Program 2
print("")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C3 = A.intersection(B)
print(C3)
print("")

#Program 3:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.issubset(B))
print("")

#Program 4:
print(A.isdisjoint(B))
print("")

#Nivel 3
#Program 5:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.union(B))
print("")

#Program 6:
print(A.symmetric_difference(B))
print("")

#Program 7:
del A
del B
print("")