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
