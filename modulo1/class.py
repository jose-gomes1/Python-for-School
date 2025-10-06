import os

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, year):
        Person.__init__(self, name, age)
        self.year = year


p1 = Person("John", 36)
p2 = Student("A", 18, 12)

class Carro:

    acelera = 0
    velocidade = 0
    velocidadeMax = 255

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
    def acelerar(self, acelera):
        self.velocidade += acelera
        if self.velocidade >= self.velocidadeMax:
            self.velocidade = self.velocidadeMax
        print(f"Acelerando a {self.velocidade} km/h")

print(p2.name, p2.age, p2.year)