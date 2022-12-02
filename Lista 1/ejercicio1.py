#1.Realizar un programa que ingrese sus datos personales e imprimirlos.

print("Ingrese su nombre completo: ")
nombre = str(input())
print("Ingrese su apellido completo: ")
apellido = str(input())
print("Ingrese su edad: ")
edad = int(input())
print("Ingrese su numéro de celular: ")
celular = str(input())

print("""Sus datos personales son: 
Nombres: """,nombre, 
"\nApellidos:", apellido, 
"\nEdad:",edad,
"\nCelular: ", celular)
