class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def mostraMarca(self):
        print(self.marca, end=" ")
    def mostraModelo(self):
        print(self.modelo)
    
c1 = Carro("Fiat", "500")
c1.mostraMarca()
c1.mostraModelo()