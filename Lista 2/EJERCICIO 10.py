"""10.Realizar un programa que realice las siguientes funciones de string al texto.
-split
-count
-find
-uppercase
-lowercase
texto=Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y
los mezcló de tal manera que logró hacer un libro de textos especimen.”"""


TEXTO ="""Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y
los mezcló de tal manera que logró hacer un libro de textos especimen."""

Separar = TEXTO.split()
print("\n\n 1) Se tiene la siguiente lista: \n\n", Separar)

conteo= TEXTO.count("texto")
print("\n 2) Hay ",conteo, "palabra texto o textos.\n ")

Encontrar=TEXTO.find('Ipsum')
print("\n 3) La palabra se encuentra despues del espacio ", Encontrar)

MAY= TEXTO.upper()
print("\n 4) EL NUEVO TEXTO EN MAYUSCULA ES: ", MAY)

MIN= TEXTO.lower()
print("\n 6) EL NUEVO TEXTO EN MINUSCULA ES: ", MIN)