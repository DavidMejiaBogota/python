#Pseudocódigo

# Instrucciones FOR IN

# PARA CADA ELEMENTO HACER
#   Instruccines
# Fin del For In (Hacer)

# Ejemplo:

mi_lista = ['Luis', 'José', 'David', 'John']
str_cadena = "Bucle For In"
print("\n" + str_cadena.center(50, "/") + "\n")

for nombre in mi_lista:
    print(nombre)


#Pseudocódigo

# Instrucciones WHILE

# Hacer Mientras condición
#   instrucciones
# Fin del Hacer Mientras

# Ejemplo

int_indice = 0

str_cadena = "Bucle For In con While"
print("\n" + str_cadena.center(50, "#"))

while int_indice < len (mi_lista):
    print(mi_lista[int_indice])
    int_indice = int_indice + 1
