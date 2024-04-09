#Paso a pasa: Ejercicio de desafío con operadores aritméticos

# 1 Definir 4 variables del tipo String manualmente (sin solicitarlas al usuario)

str_Precio1 = "11111111"
str_Precio2 = "22222222"
str_Precio3 = "33333333"
str_Precio4 = "44444444"

# 2 Transformar cada valor en un entero y sumarlos en una variable: ( La suma no debe ser mayor a 999.999.999)

int_Total = int(str_Precio1) + int(str_Precio2) + int(str_Precio3) + int(str_Precio4)

print("El valor de la suma de las cuatro varibles (Precio 1 al 4) es: %d" %(int_Total))

# 3 calcular la parte entera y la parte decimal como se explicó en ejercicios anteriores: (6E+3D)

int_Parte_Entera = int_Total / 1000
int_Parte_Decimal = int_Total % 1000

# 4 mostrar el mensaje con el rusultado en pantalla representando el número completo con sus decimales

print("Precio(6E+3D): %d.%0.3d" %(int_Parte_Entera,int_Parte_Decimal))
