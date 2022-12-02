"""8.Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el
usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas"""

import math
print("ingrese el numero:")
clave = "contraseña"
contraseña = input ("introduce la contraseña")
if clave == contraseña.lower():
    print("la contraseña coincide")
else:
    print("la contraseña no coincide")
    