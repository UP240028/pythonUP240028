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
