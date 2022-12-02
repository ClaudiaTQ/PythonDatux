#7. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos:
#Si los dos números son iguales
#Si los dos números son diferentes
#Si el primero es mayor que el segundo
#Si el segundo es mayor o igual que el primero

número1 = float( input( "Introduce el primer número: "))
número2 = float( input( "Introduce el segundo número: "))

print( "¿Los números son iguales?:", número1 == número2)
print( "¿Los números son diferentes?:", número1 != número2)
print( "¿El primer número es mayor que el segundo?:", número1 > número2)
print( "¿El segundo número es mayor o igual que el primero?:", número2 >= número2)