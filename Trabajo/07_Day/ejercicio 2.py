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