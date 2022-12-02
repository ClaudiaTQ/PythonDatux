#9.Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

print("Ingrese un número entero: ")
num=int(input())

if num%2== 0:
    print("El número ",num, "es par")
else:
    print("El número ",num, "es impar")