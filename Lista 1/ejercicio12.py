#Defina una lista de 5 estudiantes realice lo siguiente :
#el tamaño de la lista.listo
#el ultimo elemento.listo
#Revierta los elementos.
def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li






# bloque principal del programa
lista=carga_lista()
print("El número de elementos de la lista  es:",
      len(lista))
print(lista)
print("El ultimo número de  la lista  es:")
print(lista[-1])
lista2=lista[::-1]
print(lista2)  
