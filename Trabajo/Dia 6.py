#ejercio 1
print("")
empty=()

#ejercicio 2
print("")
print("Dos listas de nombres de mis hermanos:")
Sisters=("Estrella", "Sarai")
brothers=("Rafael", "Juanito", "Piratita")
print("Lista de hermanas",Sisters)
print("Lista de mis hermanos: ", brothers)

#ejercicio 3
print("")
print("Lista unida de hermanos")
siblings= Sisters + brothers
print(siblings)

#ejercio 4
print("")
print("¿Cuantos hermanos tengo?")
n_siblings= len(siblings)
print(n_siblings)

#ejrcio 5
print("")
family_members=siblings + ("Tio Gallo", "Tia Polla")
print(family_members)

#Nivel 2
#ejercicio 1
print("")
family_members= list(family_members)
del family_members[5:7]
print("Lista modificada,Padres borrados: ")
print(family_members)

#ejercicio 2
print("")
print("Nuevas cadenas:")
fruits=("Naranja", "Limon", "Manzana", "Bananas")
vegetables=("Lechuga", "Zanahorias", "Cebolla", "Rabano")

