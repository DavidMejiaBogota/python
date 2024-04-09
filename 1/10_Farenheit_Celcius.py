#Enunciado

#Realice un programa que solicite al usuario los datos para llevar a Grados Farenheit a Grados Celcius.

#Solución

#Definición/inicialización de variables

int_Farenheit = 0
float_Celcius = 0.0

#Inicio del programa

print("Llevar de Farenhtint a Celcius")

#Solicitud de datos al usuario:
int_Farenheit = int(input('Por favor ingrese el valor de los grados Farenheit: '))

#Formula para pasar de grados Farenheit a Celcius: Celcius = (farenheit - 32.0) * 5.0/9.0

float_Celcius = (int_Farenheit-32.0) * 5.0/9.0
print("Grados Celcius: %0.2f" %(float_Celcius))
