#1
print("")
print("#Programa 1")
age= int(input("Escribe tu edad: "))

##2
print("")
print("#Programa 2")
height=float(input("Escribe tu alrtura: "))

##3
print("")
print("#Programa 3")

complex = complex(input("Un numero complejo: "))

##4 triangle

print("")
print("#Programa 4")
base = int(input("Ingresa la base del triangulo: "))
heightT= int(input("Ingresa la altura del triangul: "))
area= float(( base * heightT)/2)
print("E l area de un triangulo es: ", area )

#5

print("")
print("#Programa 5")
print("Perimetro de un triangulo")

sideA= int(input("ingresa el lado A del triangulo: "))
sideB=int(input("Ingresa el lado B del triangulo: "))
sideC= int(input("Ingresa el lado C del triangulo: "))
perimeter=int( sideA + sideB + sideC)
print("El perimetro del triangulo es: ", perimeter)

#6

print("")
print("#Programa 6")
print("Area de un rectangulo")

length= int(input("Ingresa el largo del rectangulo: "))
width= int(input( "Ingresa el ancho del rectangulo: "))
areaRec= int( length * width)
perimeterRec= int( (length + width)*2)
print("El area del rectangulo: ", areaRec)
print("El perimetro del rectangulo es: ", perimeterRec)

#7

print("")
print("#Programa 7")
print("Area y circunferencia de un circulo")

radius= int(input("Ingresa el radio del circulo: "))
pi=3.14
areaCir= float(pi * (radius * radius))
circumference=float(2 * pi * radius)
print("El area del circulo es: ", areaCir)
print("La circunferencia del circulo es: ", circumference)

#8

print("")
print("#Programa 8")
print("Interseccion de la pendiente")
pendiente= 2 #la pendiente de la ecuacion
intY= -2 #Interaccion con ele Y
intX= (intY / pendiente) #Interaccion con eje X
print( "La pendiente de la ecuacion es: ",pendiente)
print("La interaccion es de: ", intX)

#9

print("")
print("#Programa 9")
ejeX1=2 #el valor de x1
ejeY1=2 #el valor de y1
ejeX2=6 #el valor de x2
ejeY2=10 #el valor de y2
pendienteM=float(ejeY2 -ejeY1 / ejeX2 - ejeX1)
velocidadEcl=float((ejeY2-ejeY2)**2 / (ejeX2-ejeX1)**2)**0.5
print("La pendiente es: ", pendienteM)
print("La velocidad eclidiana es: ",velocidadEcl)

#10 Compare the slopes

print("")
print("#Programa 10")
print("Vamos a comparar pendientes")
compare= pendiente >= pendienteM
print("¿La copmparacion indica que la primer pendiente es mayor o igual que la segunda?: ", compare )

#11 Calcular valor de Y

print("#Programa 11")
X1=1
Y1= (X1**2) + (6*X1) + 9
print("cuando X vale 1 obtenemos que Y vale: ", Y1) 
print( " Vemos que cuando son valores positivos se va demasiado del 0")
print( " Asi que es mejor intentar con los negatvos")
X4=-1
Y4= (X4**2) + (6*X4) + 9
print("cuando x vale -1 obtenemos que Y vale: ",Y4)
X2= -2
Y2= (X2**2) + (6*X2) + 9
print("cuando X vale -2 obtenemos que Y vale: ", Y2)
X3=-3
Y3= (X3**2)+ (6*X3) + 9
print("Cuando X vale -3 obtenemos que Y vale: ", Y3)

#12 Comparacion de titanes

print("")
print("#Programa 12")
phyton= 2
dragon= 3
PhyandDragon= phyton>dragon
print(" ¿ES verdad que dragon es mas vergas que phyton? ")
print(PhyandDragon)

#13 
print("")
print("#Proframa 13")
print("¿On esta en dragon o phyton?")
dragono="on"
phyton1= "luis"
if "on" in phyton1:
    print( "no esta en phyton")
else:
    print("On esta en Dragon")

#14

print("#Programa 14")
print("¿esta jerga en la siguinte oracion?")
print("espero que este curso no este lleno de jerga")
sentence="espero que este curso no este lleno de jerga "
if "jerga" in sentence:
    print("si esta jerga en la oracion")
else:
    print( "No no esta jerga en la oracion")

#15
print("")
print("#Programa 15")
dragon15= "Peso pluma es el mas duro de mexico"
phyton15= "El anciano ya no hace partidos en el ejido"
print("Tengo dos oraciones, ¿Cual deice encendido?")
print("phyton:",phyton15)
print("dragon:", dragon15)
if "encencido" in dragon15:
     print("La palabra encendido esta en dragon")
if "encendido " in phyton15:
    print("La palabra esta en phyton")
else:
    print("No esta en ninguna de las dos")

#16

print("")
print("#Programa 16")
print("Longitud del texto de la variable phyton")
phyton16="Esta clase dura una hora y he aventajado poco"
print(len(phyton16))
print(len(phyton16))

#17

print("")
print("#Programa 17")

numero17=int(input("Ingresa un Numero entero para saber si es par: "))
if numero17 % 2 == 0:
    print("tu numero es PAR")
else:
    print("Tu numero no es PAR")

#18

print("")
print("#Programa 18")
print("¡La division del piso de 7x3 es igual al valor init convertido de 2.7?")

print(7//3 == int(2.7))

#19
print("")
print("#Programa 19")
print("¿El typo 10 es igual a 10?")
print(type(10) == 10) 

#20
print("")
print("#Programa 20")
print("¿El entero de 9.8 es igual a 10?")
print(int(9.8)==10)

#21
print("")
print("#Programa 21")
print("Calcula tu paga")
horas=int(input("ingresa las horas trabajadas: "))
tarifa=int(input("ingresa tu tarifa por hora: "))
paga= (horas * tarifa)
print("Tu paga es de : ",paga)

#22
print("")
print("#Programa 23")
print("Checa cuanto te queda de vida")
añosactuales= int(input("Ingrese su edad actual: "))
edadestablecida= 100
añosrestantes= (edadestablecida -añosactuales)
vidarestante= añosrestantes*365*24*3600
print("tu vida restante es de: ", vidarestante )

#23
print("")
print("#Programa 23")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print(" 5 1 5 25")

print("Revisado")