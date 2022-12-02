#8. Definir una función que imprima los argumentos ingresados desde linea de comandos
#Nota: Usar import sys.argv => *args

import sys
def indeterminados_posicion(*args):
    for arg in args:
        print(arg)


indeterminados_posicion(sys.argv)