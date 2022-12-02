"""11.Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un
menú:
● Mostrar una suma de los dos números
● Mostrar una resta de los dos números (el primero menos el segundo)
● Mostrar una multiplicación de los dos números
● En caso de introducir una opción inválida, el programa informará de que no es correcta."""

num1 = float(input("Ingresa un número: ") )
num2 = float(input("Ingresa otro número: ") )
opcion = 0

print("Elegir una de las opciones:  \n1) Su1mar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
opcion = int(input("Ingresa un número: ") )     

if opcion == 1:
    print("La suma de",num1,"+",num2,"es",num1+num2)
elif opcion == 2:
    print("La resta de",num1,"-",num2,"es",num1-num2)
elif opcion == 3:
    print("El producto de",num1,"*",num2,"es",num1*num2)
else:
    print("Opción incorrecta")




