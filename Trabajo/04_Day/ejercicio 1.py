#Programa 1
print("")
first_word= "Treinta"
second_word= "Dias"
thir_word="De"
fourth_word= "Phyton"
space=" "
full_Sentence= first_word + space + second_word + space + thir_word + space + fourth_word
print(full_Sentence)
 
 #Programa 2
print("")
firstword= "Codificacion"
secondword= "Para"
thirdword="Todos"
full_Sentence2= firstword + space + secondword + space + thirdword
print(full_Sentence2)

#Programa 4
print("")
company= "Codificacion para todos"

#Programa 5 
print("")
print("Longitud de variable: ")
print(len(company))

#Programa 6
print("")
print("Cambiando caracteres a mayuscula: ")
company1= company.upper()
print(company1)

#Programa 7
print("")
print("Cambiando caracteres a minisculas: ")
company2= company.lower()
print(company2)

#Programa 8 
print("")
print("Capitalizar sentence: ")
company_capitalizar= company.capitalize()
print(company_capitalizar)
print("")
print(" Titular sentence: ")
company_titular= company.title()
print(company_titular)
print("")
print("Swapcase sentence: ")
company_swapcase= company.swapcase()
print(company_swapcase)

#Programa 9
print("")
print("Cortar la primera palabra")
company_cut= (company.split("Codificacion"))
print((company_cut))

#Programa 10
print("")
print("Esta presente la palabra Codificacion")
if "Codificacion" in company:
    print("La palabra codificacion se encuentra en la posicion")
else:
    print("La palabra Codificacion no se encuentra")

#Programa 11
print("")
print("texto original: ",company)
print(("Remplazando texto: "))
companyTwo= company.replace("Codificacion","Phyton")
print(companyTwo)

#Programa 12

print("")
print(companyTwo)
print("Cambiando el resto del texto: ")
companyThree=companyTwo.replace("para todos","para todo el mundo")
print(companyThree)

#Programa 13
print("")
companysplit= (company.split())
print(companysplit)

#Programa 14
print("")
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(", ")
print(split_companies)

#Programa 15
print("")
print("caracter en indice 0: ")
caracter_en_indice_0 = company[0]
print(caracter_en_indice_0)

#Programa 16
print("")
print("ultimo indice: ")
ultimo_indice = company[-1]
print(ultimo_indice)

# Programa 17
print("")
print("Indice en la posicion 10: ")
diez_indice = company[10]
print(diez_indice)

#Programa 18
print("")
print("Acronimo de Phyton for everyone: ")
phrase = "Python For Everyone"
acronym = (phrase[0]+phrase[7]+phrase[11]).upper()
print(acronym)

#Programa 19
print("")
print("Abrebiatura de Coding for all: ")
name="Coding For All"
acronym2= (name[0] + name[7] + name[11]).upper()
print(acronym2)

#Programa 20
print("")
print(name)
position = name.index('C')
print("La posición de la primera ocurrencia de 'C' es: ", position)

#Programa 21
print("")
print(name)
position1 = name.index('F')
print("La posición de la primera ocurrencia de 'F' es: ", position1)

#Programa 22
print("")
print(name)
position2 = name.rfind('i')
print("La posición de la ultima ocurrencia de 'i' es: ", position2)

#Programa 23
print("")
phrase1="You cannot end a sentence with because because because is a conjunction"
print(phrase1)
position3 = phrase1.index('because')
print("La posición de la primera ocurrencia de 'because' es: ", position3)

#Programa 24
print("")
print(phrase1)
position4 = phrase1.rindex('because')
print("La posición de la ultima ocurrencia de 'because' es: ", position4)

#Programa 25
print("")
print(phrase1)
phrase_extracted= phrase1[30:54]
print("la frase ectraida de la oracion es: ")
print(phrase_extracted)

#Programa 26
print("")
print(phrase1)
position3 = phrase1.index('because')
print("La posición de la primera ocurrencia de 'because' es: ", position3)

#Programa 27
print("")
print(phrase1)
phrase_extracted= phrase1[30:54]
print("la frase ectraida de la oracion es: ")
print(phrase_extracted)

#Programa 28
print("")
print(name)
starts_with_coding = name.startswith('Coding')
print("¿La cadena comienza con 'Coding'? ", starts_with_coding)

#Programa 29
print("")
print(name)
end_with_coding= name.endswith("Coding")
print("¿La cadena termina con 'Coding'? ", end_with_coding)

#Programa 30
print("")
sentence=' Coding For All ' 
clean_sentence= sentence.strip( )
print("La cadena limpiada de los espacios inecesarios es: ",clean_sentence)

#Programa 31
print("")
print("Identificacion de variables no validas")
var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
print("La variable 1 es valida: ", var1, "Es: ",var1.isidentifier())
print("La variable 2 es valida: ", var2, "Es: ",var2.isidentifier())

#Programa 32
print("")
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print(joined_libraries)

#Programa 33
print("")
print("Use the new line escape sequence to separate the following sentences.")
sentence1 = "I am enjoying this challenge.\nI just wonder what is next."
print(sentence)

#Programa 34
print("")
print("Use a tab escape sequence to write the following lines")
table = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(table)

#Programa35
print("")
print("Metodo de cadena")
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

#Programa 36
print("")
print("Use the string formatting method to display the following:")
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

print("Revisado")