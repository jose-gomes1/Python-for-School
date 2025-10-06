import os

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

class Carro:
    def __init__(self, marca, modelo, km):
        self.marca = marca
        self.modelo = modelo
        self.km = km
    def mostraMarca(self):
        print(self.marca, end=" ")
    def mostraModelo(self):
        print(self.modelo)
    def conduz(self):
        a = input("Aperte Enter para continuar ou 'n' para parar")
        while a != "n":
            print(f"{self.km} km andados")
            self.km += 1
            if self.km % 10 == 0:
                os.system("clear")
            a = input("Aperte Enter para continuar ou 'n' para parar")
        print(f"{self.km} km andados")
    
c1 = Carro("Fiat", "500", 0)
c1.conduz()