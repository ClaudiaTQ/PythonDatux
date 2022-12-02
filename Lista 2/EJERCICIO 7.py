#7. Definir una función que retorne el mayor valor al ingresar 2 números#
def mayor ():
 print("ingresa un numero")
 n1=int(input("numero 1:"))
 n2=int(input("numero 1:"))
 if n1==n2:
    print("Los numeros son iguales")
 elif n1>n2:
    print("El numero ",n1, "es mayor a" ,n2,"")
 else:
    print("El numero", n2, "es mayor a" ,n1,"")
resultado=mayor()
print(resultado)