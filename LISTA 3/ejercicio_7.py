"""7.Hacer un programa que consulte el valor del dolar (compra y venta ) de la fecha actual
segun sunat (url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat')"""


def EJ7(): 
    import requests
    from bs4 import BeautifulSoup as b
    response = requests.get("https://api.apis.net.pe/v1/tipo-cambio-sunat")
    response.json() 
    data = response.json()
    compra = data['compra']
    venta = data['venta']
    fecha = data['fecha']
    print("El valor del dolar en la compra es: ",compra)
    print("El valor del dolar en la venta es: ",venta)
    print("La fecha del cambio actual del dolara es: ",fecha)
    print("\nFin de ejecucion\n")