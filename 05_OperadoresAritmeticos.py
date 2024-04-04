#Operadores Aritméticos

#Variables:
# int_Nombre_variable = tipo_dato       ;   Variable de tipo entero
# float_Nombre_variable = tipo_dato     ;   Variable con decimiales
# str_Nombre_variable = tipo_dato       ;   Variable con cedenas o caracteres
# bool_Nombre_variable = tipo_dato      ;   Variables booleanas


#Constantes:
#const_Nombre_Constante = tipo_dat      ;   Constante de cualquier tipo de dato

#Principales Operadores aritméticos:

# Símbolo   Significado     Ejemplo             Resultado
# +         Suma            a = 10 + 5          a es 15
# -         Resta           a = 12 - 7          a es 5
# *         Multiplicación  a = 7 * 5           a es 35
# **        Exponente       a = 2 ** 3          a es 8
# /         División        a = 12.5 / 2        a es 6.25
# //        División entera a = 12. // 2        a es 6
# %         Módulo          a = 7 / 2           a es 1

# Formato Moneda
# Trama = 6E.3D

#Declaración de variables

str_Trama = "2500000777"    # 6E+3D = 250000.777
int_Parte_Entera = 0        # 6E
int_Parte_Deceimal = 0      # 6D

#Programa Principal

print("")
print("******FORMAR TRAMA******")
print("")
print("************************")
print("Trama Inicial: %s"%(str_Trama))
print("************************")
print("")

int_Parte_Entera = int(str_Trama)/1000
print("Parte entera  (6E): %d" %(int_Parte_Entera))
int_Parte_Decimal = int(str_Trama) % 1000
print("Parte decimal (3D): %d" %(int_Parte_Decimal))
print("")

print("************************")
print("Precio(6E+3D): %d.%d" %(int_Parte_Entera,int_Parte_Decimal))
print("************************")
