# ejercicio 1
print("")
print("Lista vacia")
mi_lista=[]
print(mi_lista)

#ejercicio 2
print("")
print("Lista de nnumeros:")
numbers=[10, 20, 30, 40, 50, 60]
print(numbers)

#ejercicio 3
print("")
print("Longitud de la lista:")
longitud_numbers= len(numbers)
print(longitud_numbers)

#ejercicio 4
print("")
first_item = numbers[0]
middle_item = numbers[len(numbers) // 2]
last_item = numbers[-1]
print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)

#ejercicio 5
print("")
mixed_data_types=["Angel", 18, 1.75, "Soltero", "Calle 20 de noviembre"]

#ejercicio 6 
print("")
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#ejercicio 7 
print("")
print("Lista de compañias: ")
print(it_companies)

#ejercicio 8
print("")
print("Numero de empresas:")
n_companies= len(it_companies)
print(n_companies)

#ejercicio 9 
print("")
f_comp=it_companies[0]
m_comp=it_companies[len(it_companies)//2]
l_comp=it_companies[-1]
print("La primera compañia es: ",f_comp)
print("La compañia del medio es: ",m_comp)
print("La ultima compañia de la lista es: ",l_comp)

#ejercicio 10
print("")
print("Lista modificada: ")
it_companies[2]= "Tesla"
print(it_companies)

#ejercicio 11
print("")
print("Agregar empresa: ")
it_companies.append("Meta")
print(it_companies)

#ejercicio 12
print("")
print("Agrer empresa en el centro")
it_companies.insert(4, "Youtube")
print(it_companies)

#ejercicio 13
print("")
print("Cambiar los valores de la lista a mayusculas exepto IBM")
for i in range(len(it_companies)):
    if it_companies[i] != "IBM":
        it_companies[i] = it_companies[i].upper()
        break  
print(it_companies)

#ejercicio 14
print("")
joined_companies = "#;  ".join(it_companies)
print("Compañias unidas:", joined_companies)

#ejercicio 15
print("")
verificacion = "Apple"
if verificacion in it_companies:
    print(f"{verificacion} existe en la lista")
else:
    print(f"{verificacion} no existe en la lista")

#ejercicio 16
print("")
it_companies.sort()
print("lista ordenada de empresas:")
print(it_companies)

#ejercicio 17
print("")
print("Inviertir la lista en orden descendente: ")
it_companies.sort()
print("lista de empresas: ")
print(it_companies)

#ejercicio 18
print("")
print("Separa las primeras 3 empresas de la lista: ")
first_3_companies = it_companies[:3]
print("Primeras 3 companias:", first_3_companies)

#ejercicio 19 
print("")
print("Eliminar las últimas 3 empresas de la lista: ")
last_3_companies = it_companies[-3:]
print("Last 3 companies:", last_3_companies)

#ejercicio 20
print("")
print("Eliminar de la lista las empresas de TI intermedias")
it_companies = [it_companies[0], it_companies[-1]]
print("Lista de empresas de TI después de eliminar las intermedias:", it_companies)

#ejercicio 21
print("")
print("Eliminar la primera empresa de TI de la lista")
it_companies.pop(0)
print("Lista después de eliminar la primera empresa:", it_companies)

#ejercicio 22
print("")
print("Eliminar la empresa de TI intermedias de la lista")
it_companies = [it_companies[0], it_companies[-1]]
print("Lista después de eliminar las empresas intermedias:", it_companies)

#ejercicio 23
print("")
print("Eliminar la última empresa de TI de la lista")
it_companies.pop()
print("Lista después de eliminar la última empresa:", it_companies)

#ejercicio 24
print("")
print("Eliminar todas las empresas de TI de la lista")
it_companies.clear()
print("Lista después de eliminar todas las empresas:", it_companies)

#ejercicio 25
print("")
print("Destruir la lista de empresas de TI")
del it_companies
try:
    print(it_companies)
except NameError:
    print("La lista ha sido destruida y ya no existe.")

#ejercicio 26
print("")
print("Únase a las siguientes listas: ")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end.extend(back_end)
print("Full Stack:", front_end)

#ejercicio 27
print("")
print("Asignar a variable: ")
full_stack = front_end + back_end
full_stack_copy = full_stack.copy()
index_of_redux = full_stack_copy.index('Redux')  
full_stack_copy.insert(index_of_redux + 1, 'Python')
full_stack_copy.insert(index_of_redux + 2, 'SQL')
print("Lista completa con Python y SQL:", full_stack_copy)

print("Revisado")