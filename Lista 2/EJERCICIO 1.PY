# 1.Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el
#número

def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li


def imprimir_mult2(li):
    print("Lista de elementos")
    for x in range(len(li)):
        if li [x]%2 ==0:
           print ("es multiplo de 2")
        else:
            print("no es multiplo de 2")
            print(li[x])



# bloque principal del programa
lista=carga_lista()
print(lista)
imprimir_mult2(lista)