# #Declaração de variáveis

# idade = 17
# nome = "José"
# altura = 1,70
# estudante = True

# #Operadores aritméticos

# print(idade + 1)
# print(idade - 1)
# print(idade / 2)
# print(idade * 2)

# #Operadores de comparação
# print(idade > 18)
# print(idade == 18)
# print(idade != 18)
# print(idade <= 18)
# print(idade >= 18)
# print(idade >= 18 and estudante)
# print(idade >= 18 or estudante)
# print(not estudante)

# #Instruções condicionais

# idade = int(input("Qual a tua idade? "))

# if idade < 18:
#     print("Menor de idade")
# elif idade > 18:
#     print("Maior de idade")
# else:
#     print("Acabaste de fazer 18")

# #Laços de repetição (cíclos)

# for i in range(2, 10, 2):
#     print("Loop", i)

# i = 0
# while i<10:
#     print("Repetição", i)
#     i += 1

# #do while não existe em Python

#Funções (Programação Funcional)

def repetir(x):
    i = 0
    while i <= 10:
        print("Loop", i)
        i += x
    return i

def repetirV(vezes, x):
    i = 0
    while i <= vezes:
        print("Loop", i, "de", vezes)
        i += x
    return

#Funções com retorno

def somar(a,b):
    return a + b
resultado = somar(5,3)

# repetir(2)
# repetirV(10,5)
# print(resultado)

#Bibliotecas
import math

raiz = math.sqrt(16)
print("Raiz quadrada de 16 é", raiz)
potencia = math.pow(2, 5)
print("2^3 é", potencia)