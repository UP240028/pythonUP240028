#ejercicio 1y2
print("")
dog={
    "nombre":"Rufus",
    "color":"cafe",
    "raza":"Doberman",
    "patas":"cuatro",
    "edad":"Cinco años"
}
print(dog)

#ejercicio 3
print("")
estudiante={
    "nombre":"Luis",
    "apellido":"Camacho",
    "sexo":"hombre",
    "edad":"18",
    "estado civil":"Soltero",
    "habilidades":["Inteligente","Audaz"],
    "pais":"Mexico",
    "ciudad":"Tamaulipas",
    "direccion":"Calle 8 de marzo,#1235"

}

#ejercicio 4
print("")
print("Longitud del diccionario estudiante:")
print(len(estudiante))

#ejercicio 5
print("")
print("Tipo de las habilidades:")
print(type(estudiante["habilidades"]))

#ejercicio 6
print("")
estudiante["habilidades"].extend(["veloz","agil"])
print(estudiante["habilidades"])

#ejercicio 7
print("")
estudiante["Habilidades"] = "Hiper foco"
print(estudiante)

#Obtenga las claves del diccionario como una lista
Claves = estudiante.keys()
print(Claves)

#Obtener los valores del diccionario como una lista
Valores = estudiante.values()
print(Valores)

#Cambie el diccionario a una lista de tuplas usando el método items()
print(estudiante.items())

#Eliminar uno de los elementos del diccionario
estudiante.pop("Habilidades")
print(estudiante)

#Eliminar uno de los diccionarios
del dog