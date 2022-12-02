#Realizar un programa que calcule la penalidad por la mora de una deuda,sabiendo que si se
#demora de 1 día a 10 se le agrega el 5% , si se demora hasta 30 días se le agrega 8% y pasando
#el rango máximo se le agrega un 10%

print("ingrese el dia para poder calcular la penalidad por la mora:")
dia= int(input())

if 1<= dia and  dia<= 10:
    mensaje = "se le agrega 5 porciento de mora"
elif 10< dia and dia<=30:
    mensaje = "se le agrega 8 porciento de mora"
else:
    mensaje = "se le agrega 10 porciento de mora"

print(mensaje)
