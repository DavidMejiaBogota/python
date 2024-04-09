#Pseudocódigo

#Instruccion WHILE (Hcer Mientras)

# Hacer Mientras condición
#   instrucciones
#fin del Hacer Mientras

#Ejemplo:

#Declaración/inicializacion de variables

int_tabla = 13
int_numero = 1
int_resultado = 0

str_cadena = "Tabla de Multiplicar"
print("\n" + str_cadena.center(35, "*") + "\n")

while int_numero <10:
    int_resultado = int_tabla * int_numero
    print("{} * {} = {}".format(int_tabla,int_numero,int_resultado))
    int_numero = int_numero + 1



