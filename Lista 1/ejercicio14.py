#14.Realice un Menú interactivo que tenga las opciones de saludar ,una operación matemática y
#salir.


print("Menú interactivo")
while True:
    print("""Escribe una opcion 
            1) Saludar
            2) Resta
            3) Salir

     """)

    opcion=input()

    if opcion == '1':
        print("Hola mundo")
    elif opcion == '2':
        print("Ingresa dos numeros: ")
        num1=float(input("numero 1: "))
        num2=float(input("numero 2: "))
        print(f"El resultado es {num1-num2}")
    elif opcion == '3':
        break;
    else:
        print("ingrese una opción valida: ")