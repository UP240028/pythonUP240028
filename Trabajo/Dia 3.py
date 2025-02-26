#1

age= int(input("Escribe tu edad: "))

##2

height=float(input("Escribe tu alrtura: "))

##3

complex = complex(input("Un numero complejo: "))

##4 triangle

print("")
base = int(input("Ingresa la base del triangulo: "))
heightT= int(input("Ingresa la altura del triangul: "))
area= float(( base * heightT)/2)
print("E l area de un triangulo es: ", area )

#5

print("")

print("Perimetro de un triangulo")

sideA= int(input("ingresa el lado A del triangulo: "))
sideB=int(input("Ingresa el lado B del triangulo: "))
sideC= int(input("Ingresa el lado C del triangulo: "))
perimeter=int( sideA + sideB + sideC)
print("El perimetro del triangulo es: ", perimeter)

#6

print("")

print("Area de un rectangulo")

length= int(input("Ingresa el largo del rectangulo: "))
width= int(input( "Ingresa el ancho del rectangulo: "))
areaRec= int( length * width)
perimeterRec= int( (length + width)*2)
print("El area del rectangulo: ", areaRec)
print("El perimetro del rectangulo es: ", perimeterRec)

#7

print("")

print("Area y circunferencia de un circulo")

radius= int(input("Ingresa el radio del circulo: "))
pi=3.14
areaCir= float(pi * (radius * radius))
circumference=float(2 * pi * radius)
print("El area del circulo es: ", areaCir)
print("La circunferencia del circulo es: ", circumference)

#8

print("")

print("Interseccion de la pendiente")
pendiente= 2 #la pendiente de la ecuacion
intY= -2 #Interaccion con ele Y
intX= (intY / pendiente) #Interaccion con eje X
print( "La pendiente de la ecuacion es: ",pendiente)
print("La interaccion es de: ", intX)

#9

print("")
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
print("Vamos a comparar pendientes")
compare= pendiente >= pendienteM
print("¿La copmparacion indica que la primer pendiente es mayor o igual que la segunda?: ", compare )

#11 Calcular valor de Y

print("")
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

phyton= 2
dragon= 3
PhyandDragon= phyton>dragon
print(" ¿ES verdad que dragon es mas vergas que phyton? ", PhyandDragon)

#13 

print("")
dragono="on"
phyton1= "luis"
if "on" in phyton1:
    print( "no esta en phyton")
else:
    print("esta en Dragon")

