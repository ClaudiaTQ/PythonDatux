#5 Definir una función que multiplique 2 números mayores de cero

def mostrar_mensaje(mensaje):
    print("*************************************************")
    print(mensaje)
    print("*************************************************")

def carga_Mult():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    if (valor1>0 and valor2 > 0) :
     Mult=valor1*valor2

     print("La multiplicacion de los numero es:",Mult)
    elif(valor1<0 or valor2 <0 ):
        print("uno de los numeros es menor o igual a 0")

# programa principal

mostrar_mensaje("El programa calcula la multiplicacion de dos valores ingresados por teclado.")
carga_Mult()
mostrar_mensaje("Gracias por utilizar este programa")
