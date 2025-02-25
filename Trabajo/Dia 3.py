#1

age= int(input("Escribe tu edad: "))

##2

height=float(input("Escribe tu alrtura: "))

##3

complex = complex(input("Un numero complejo"))

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