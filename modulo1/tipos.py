# listas -> arrays []
# dictionary -> par chave -> valor {like:json}
# sets -> mutáveis {}
# tuplet -> imutáveis ()

# funções lambda
# funções anónimas de baixa complexidade

# exercício 1 (5m)
"""
Programa onde é definido um tuplet com 4 valores e uma função que aceita como parâmetro um tuplet e que imprime no ecrã o seu conteúdo
"""

meuTuplet = ("val1", "val2", "val3", "val4")

def funcTuplet(tuplet):
    for i in tuplet:
        b = ", ".join(tuplet)
    print(b)
    
# funcTuplet(meuTuplet)

# exercício 2
"""
Programa um programa que tenha uma função que aceita uma lista de números inteiros e devolve a soma dos seus elementos
"""

inteiros = [0, 1, 2, 3, 4]

def funcInts(lista):
    sum = 0
    for i in lista:
        sum += lista[i]
    return sum

# print(funcInts(inteiros))

# exercício 3
"""
Programa com uma função que recebe um dicionário e imprime no ecrã no seguinte formato:
chave: valor
"""

myDictionary = {"chave1":"valor1",
                "chave2":"valor2",
                "chave3":"valor3",
                "chave4":"valor4"}

def funcDictionary(dict):
    for key in dict:
        print(f"{key}:",dict[key])
    
funcDictionary(myDictionary)