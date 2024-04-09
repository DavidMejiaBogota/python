#Pseudocódigo

#Instruccionr FOR IN RANGE

# Para Cada Elemento en el Rago Hacer
#   Instrucciones
# Fin del  Hacer (Para Caelemento en el Rago Hacer)

# Ejemplo

str_cadena = "  Bucle For In Range  "
print("\n" + str_cadena.center(70, "x"))

numero = int(input("Por favor introduce el número a elevar: "))

for potencia in range(0, 11):
    resultado = numero ** potencia
    print("%d elevado a %d es %d" %(numero,potencia,resultado))
    
#Pseudocódigo

# Instrucciones While

# Hacer Mientras:
#   Instrucciones
# Fin del Hacer Mientras

# Ejemplo:

potencia = 0

str_cadena = "  Bucle For In Range con un While  "
print("\n" + str_cadena.center(70, "x"))

while potencia >=0 and potencia < 11:
    resultado = numero ** potencia
    print("%d elevado a %d es %d" %(numero,potencia,resultado))
    potencia = potencia + 1
