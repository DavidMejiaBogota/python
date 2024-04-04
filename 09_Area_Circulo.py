#Enciado
# Realice un programa que solicite al usuario los datos para calcular el área de un círculo.

#Solución:

#Definicion de constantes:
const_PI = 3.1416 #Valor aproximado

#Definición/inicializacón de variables:

int_Radio = 0
float_Area = 0

#Solicitud de datos al usuario:

int_Radio = int(input('Por favor ingrese el valor del radio del círculo: '))
#Formula para calcular el área de un círculo: Área = PI * (Radio**2)
float_Area = const_PI*(int_Radio**2)

print("El área del cícrulo es: %0.2f" %(float_Area))
