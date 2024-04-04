#Introducir datos

# ind_Nombre_variable = tipo_dato       ;   Variable de tipo entero
# float_Nombre_variable = tipo_dato     ;   Variable con decimiales
# str_Nombre_variable = tipo_dato       ;   Variable con cedenas o caracteres
# bool_Nombre_variable = tipo_dato      ;   Variables booleanas

# Pseudocódigo:

# nombre_Variable = tipo_dato
# introducir nombre_Variable
# imprime "Comentario"

# Declaración de variables

int_Edad = 0
float_Estatura = 0.0
str_Inicial = ""
str_Apellido = ""

#Inicio del programa o solicitud de datos al usuario

int_Edad = int (input('Por favor ingresa tu edad: '))
float_Estatura = float (input('Por favor ingresa tu estatura: '))
str_Inicial = str (input('Por favor ingresa en mayusucula la inicial de tu nombre: '))
str_Apellido = str (input('Por favor favor ingresa tu apellido con la inicial en mayuscula: '))

print("")
print("Los datos ingresados son: ")
print("")
print("Edad:          %d" %(int_Edad))
print("Estatura:      %1.2f" %(float_Estatura))
print("Inicial:       %s" %(str_Inicial))
print("Apellido:      %s" %(str_Apellido))
