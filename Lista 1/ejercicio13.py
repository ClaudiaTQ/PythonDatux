#13.Defina un diccionario con una tupla y una lista de elementos, modifique el ultimo elemento.

lista_edades = [("Ana", 25), ("David",18), ("Lucas", 35), ("Ximena", 30), ("Ale", 20)]


d = {}
#Se muestra el diccionario a partir de una lista de objetos tupla
for x, y in lista_edades:
    d.setdefault(x, []).append(y)
print(d)

#Modificando el ultimo elemento
lista_edades[4]= ("Pedro",10)
print(lista_edades)
