import numpy
import pandas
import scipy
import matplotlib
import plotly
import bokeh
import seaborn
import tensorflow
import nltk
import sqlalchemy

a = 87
b = 78
print(a + b)

"""
Suma (+)
Resta (-)
Negation (-)
Product (*)
Exponent (**)
Division (/)
Division enter (//)
Modulo (%)
"""

#Resumen
suma = 87 + 96
resta = 87 - 96
negation = -87
product = 87 * 96
exponent = 2**3
division = 87 / 96
modulo = 27 % 4

print(suma, resta, negation, product, exponent, division, modulo)

#Tipos de datos complejos: Tuplas, listas y diccionarios

"""Tuple: Una tupla en Python es una estructura de datos similar a una lista, pero inmutable,
lo que significa que una vez creada, no se puede modificar su contenido.
"""
nombres_asignados = ("Omar", "Martín", "Raúl", "Javier")
print(nombres_asignados)

"""
Para acceder a un dato complejo (en este caso en una tupla), se debe tener en cuenta que
la númeración inicia en 0, en este caso "Omar" estará en la poscición cero, "Martín" en la poscición 2... 
"""
#Acceder a un elemento definido en una tupla:
print(nombres_asignados[0])
print(nombres_asignados[2])
print(nombres_asignados [1:3])
print(nombres_asignados [0:4])
print(nombres_asignados [-1])
print(nombres_asignados [-3])

"""
Listas:
las listas son estructuras de datos que permiten almacenar una colección ordenada de elementos.
Se definen utilizando corchetes [] y pueden contener elementos de diferentes tipos,
como números, cadenas de texto y objetos. Las listas son mutables, lo que significa que
sus elementos pueden cambiarse, agregar nuevos elementos o eliminarlos después de su creación.
"""

marcas_asignadas = ["Apple", "Samsung", "Xiaomi", "Motorola", "Huawei"]
print(marcas_asignadas)
marcas_asignadas[2] = "BlackBerry"
print(marcas_asignadas)
print(marcas_asignadas[4])

"""
Diccionsarios:
Los diccionarios son estructuras de datos que permiten almacenar una colección de elementos,
donde cada elemento está asociado a una clave única.
Cada elemento en un diccionario consiste en un par clave-valor,
donde la clave es única y se utiliza para acceder al valor correspondiente.
Los diccionarios se definen utilizando llaves {} y separando cada par clave-valor por comas.
"""
mis_placas = {'Carro': "RCR466", 'Moto': "IZL07E", 'Patinete': 1234, 'Bicicleta': 987654, 'Panites': "OVE123"}
print(mis_placas)
print(mis_placas['Carro'])
del(mis_placas['Patinete']) #del elimina elementos del diccionario utilizando/citando/llamando la clave.
print(mis_placas)
mis_placas['Patines'] = "YUJULE0123" #Se reasigna el valor llamando la clave
print(mis_placas['Patines'])