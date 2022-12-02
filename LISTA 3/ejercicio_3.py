"""3.Crear una clase Animal ,luego una clase Perro y gato que sean hijos de Animal ,el método
de Sonido debe ser diferente"""

def EJ3():
    class Animal:
        def __init__(self,sexo):
            self.sexo=sexo
        def __str__(self):
            pass
    class Perro(Animal):
        def sonido_animal(self,sonido):
            print("El sonido del perro es:",sonido)
    class Gato(Animal):
        def sonido_animal(self,sonido):
            print("El sonido del gato es:",sonido)
    m_1 = Perro('hembra')
    m_2 = Gato('hembra')
    print("El sexo de la mascota 1 es: ",m_1.sexo)
    print("El sexo de la mascota 2 es: ",m_2.sexo)
    m_1.sonido_animal("guau")
    m_2.sonido_animal("miaow\n")
