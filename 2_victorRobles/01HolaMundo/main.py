print("Hola mundo, soy J. David Mejía M.")
print("Hello World.")

#Soy un comentario de una sola línea
print("I'm J. David Mejía M.")

"""
Soy un comentario de varias lineas
línea 2 
línea 3
línea 4
línea 5
"""

#variables
str_texto = "Repaso de Python con Victor"
str_nombre = "Edwin Mejía M."
float_altura = 1.88
int_year = 43
 
print(f"El tema a tratar es: {str_texto} por {str_nombre}. {str(int_year)} años")

#Entrada de datos
sitioWeb = input("Ingresa tu sitio web: ")
print(sitioWeb)

#Funciones
def mostarAltura(): 
#Condiciones
    float_altura = float(input("¿Cuál es tu altura?"))
    if float_altura >= 1.80:
        print("Eres una persona alta para el promedio en Colombia")
    else:
        print("Estás en el promedio de estatura de Colombia")
mostarAltura()
mostarAltura()
mostarAltura()

#listas 

personas = ["Hugo", "Javier", "Carlos"]

print(personas)
print(personas[0])

for i in personas:
    print("persona: ", i)