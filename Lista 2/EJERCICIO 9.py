#9. Realizar una función que tenga por parámetro un lista de numerosy aumente cada
#elemento en +1
def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor+1)
    return li






# bloque principal del programa
lista=carga_lista()
print(lista)
