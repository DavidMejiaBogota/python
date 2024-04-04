#Enunciado
# Realice un programa que solicite al usuario los datos para calcular el áre de un Triángulo.

#Solucion

#Definición/inicialización de variables

int_Base = 0
int_Altura = 0
float_Area = 0.0

#Inicio del programa

print("Calcular el área del triángulo")

int_Base = int(input('Por favor ingrese el la base del triángulo: '))
int_Altura = int(input('POr favor ingrese la altura del triángulo: '))

#Formula para calcular el área de un triángulo: Area = (base*altura)/2

float_Area = (int_Base*int_Altura) / 2

print("El área del triángulo es de: %0.2f" %(float_Area))
