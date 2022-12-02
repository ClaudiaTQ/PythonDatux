#11. Definir los atributos y métodos de una de las siguientes clases.
#- Persona
#- Gato
#- Producto# ejemplo de clase

class Persona: #Creamos la clase Persona
    #definir  el metodo constructor
    def __init__(self, edad, nombre, ocupacion): #Definimos el parametro edad , nombre y ocupacion
        self.edad = edad # Definimos que el atributo edad, sera la edad asignada
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asig
        self.ocupacion = ocupacion #DEFINIMOS EL ATRIBUTO DE INSTANCIA OCUPACION
        
        #Creación de un nuevo método
    def presentar(self):
        presentacion = ("Hola soy {}, mi edad es {} y mi ocupación es {}") #Mensaje
        print(presentacion.format(self.nombre, self.edad, self.ocupacion)) #Usamos FORMAT
        print("Hola soy ",self.nombre," mi edad es",self.edad, " y mi ocupación es ",self.ocupacion)
#end class

# crear objeto de la clase Persona  
p1 = Persona(31, "Pedro", "Desocupado") #Instancia
print("*****************************")
p1.presentar()
print("*****************************")

print("Datos Persona")
print("Nombre :",p1.nombre)
print("Edad :",p1.edad)
print("Ocupacion :",p1.ocupacion)
