# Sugerido pelo Professor

# Numero 1:
"""
Implementa, em Python, um programa que faça o seguinte:
    Dada uma lista com 20 elementos, imprima no ecrã os elementos 12 a 16
"""

lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

def ex1():
    for i in range(11, 16, 1):
        print(i)


# Numero 2:
"""
Dado uma lista, elabora um programa que permita com um ciclo, inserir elementos na lista até que a tecla 'q' seja precionada
"""

def ex2():
    while True:
            a = input("O que deseja comprar? ('q' para sair) ")
            if a.lower() == 'q':
                print("Esta é a tua lista: ")
                for i in lista:
                    b = ", ".join(lista)
                print(b)
                break
            elif a:
                if a.lower() in lista:
                    print(f"{a} já está na lista")
                else:
                    lista.append(a.lower())

# Numero 3:
"""
Função que imprime a sequencia de Fibonacci até a um input
"""

def ex3():
    
    numero = int(input("Qual o digito para começar? "))
    if numero <= 1:
        print("Este número não se insere na função")
        numero = print("Insira outro: ")
    
    numero2 = int(input("Qual o digito para acabar? "))
    if numero2 <= 1:
        print("Este número não se insere na função")
        numero2 = print("Insira outro: ")
    

    a, b = 0, 1  # F1 = a = 0, F2 = b = 1

    for x in range(numero - 1):
        a, b = b, a + b

    for i in range(numero, numero2 + 1):
        print(f"F({i}) = {a}")
        a, b = b, a + b

