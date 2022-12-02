#15.iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de
#edad.
#Nota : cada elemento de la lista puede ser otra lista [[nombre,edad],.... ]

lista=[["Persona1",15],["Persona2",25],["Persona3",30],["Persona4",10]]
for elemento in lista:
    if elemento[1]>=18:
        print("Esta persona es mayor de edad: ",elemento[0])