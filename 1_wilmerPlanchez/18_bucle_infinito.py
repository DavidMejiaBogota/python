#Pseudocódigo

# Instruccion WHILE

# Hacer Mientras condicion
#   instrucciones
# Fin de Hacer Mientras

#Ejemplo:

int_intentos = 0
str_clave = "ABC123"
str_cadena = "Bucle Infinitoooooo......"

print("\n" + str_cadena.center(50, "/")+ "\n")

while True:
    str_password = input("Por favor ingrese su clave: ")

    #Contador
    int_intentos = int_intentos +1
    
    if str_password == str_clave:
        print("La clave es correcta!\n")
        int_intestos = 0
        break

    elif int_intentos == 3:
        print("Usuario Bloqueado\n")
        break
    else:
        print("Clave incorrecta intento: {}\n".format(int_intentos))

print("".center(50, "/"))
