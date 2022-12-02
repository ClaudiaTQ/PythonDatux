# 6.Realice un programa que calcule la suma de los números hasta el valor ingresado.
#  Ejemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5.

import math
print("ingrese el numero:")
n = float(input())
a = (n * (n+1))/2
print("La suma de numeros hasta ",n,"es :",a)
