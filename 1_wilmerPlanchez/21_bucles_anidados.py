#Pseudocódigo

# Hacer_1 Mientras
#   Hacer_2 Mientras
#       Hacer_3 Mientras
#       Fin Hacer_3 Mientras
#   Fin Hacer_2 Mientras
# Fin Hacer_1 Mientras

#Enunciado

#Imprimir diez veces la serie de números del 1 al 10, estos deben aparecer cada segundo

#Estudio previo

# La secuencia de númeross del 1 al 10 se realiza mediante un ciclo que vaya del 1 al 10 y un contador para generarlos

# Esta secuencia se debe realizar 10 veces por lo tanto se requiere de otro ciclo que cuente las veces que se ha inmpreso el bucle interno.
# Este ciclo aumentará en una unidad cuando se hayan visualizado los números del 1 al 10.

# El bucle exterior contro que se imprima 10 veces el bucle interior.

#Pseudocódigo

# numero = 0
# serie = 1

# Hacer_1 Mientras serie <=10

#   numero = 1

#   Hacer_2 Mientras nunero  <=10
#   Fin Hacer_2

# Fin Hacer_1 mientras

#inicio del programa

# Se importa el módulo time
import time


# Declaración de variables

int_numero = 0
int_serie = 1


while int_serie <= 12:

    if int_serie <=10:
        print("\nSerie número: %d \n" %int_serie)
        
    int_numero = 1
    
    while int_numero <=10:
        print(int_numero)
        int_numero = int_numero + 1
        
        
    int_serie = int_serie + 1
    time.sleep(1)
    print("")
