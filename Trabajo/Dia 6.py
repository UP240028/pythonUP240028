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
p_animal=("leche", "Queso","Salchicha", "Jamon")
food_stuff_tp= fruits + vegetables + p_animal
print(food_stuff_tp)

#ejercicio 3
print("")
food_stuff_it=list(food_stuff_tp)
print(food_stuff_it)

#ejercicio 4
print("")
del food_stuff_it[4:8]
print(food_stuff_it)

#ejercicio 5
print("")
del food_stuff_it[0:3]
print(food_stuff_it)
del food_stuff_it[2:6]
print(food_stuff_it)

#ejercicio 6
print("")
del food_stuff_it
print("La variable ya no existe")

#ejercicio 7
print("")
paises_nordicos=("Denmark","Iceland", "finland","Noeway", "Sweden")
print("¿Estonia es un pais nordico?")
print("Estonia" in paises_nordicos)
print("")
print("¿Iceland es un pais nordico?")
print("Iceland" in paises_nordicos)
